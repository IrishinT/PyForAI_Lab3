from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QComboBox, QFormLayout, QLabel, QLineEdit, QMainWindow, QProgressBar, QPushButton, QTabWidget,
    QVBoxLayout, QWidget,
)

from desktop.worker import PredictWorker
from ml.predictor import Predictor
from services.prediction_service import PredictionService


class MainWindow(QMainWindow):
    INITIAL_RESULT = "Результат появится здесь"
    FEATURES = (
        ("Возраст заёмщика, лет", "35"),
        ("Доход заёмщика, ден. ед.", "60000"),
        ("Сумма кредита, ден. ед.", "25000"),
        ("Срок кредита, месяцев", "24"),
        ("Количество предыдущих кредитов", "2"),
        ("Количество просроченных платежей", "1"),
        ("Трудовой стаж, лет", "10"),
    )

    def __init__(self, predictors: dict[str, Predictor]):
        super().__init__()
        self.predictors = predictors
        self.worker = None
        self.close_requested = False
        self.setWindowTitle("Кредитный скоринг")
        self.resize(500, 390)

        panel = QWidget()
        self.setCentralWidget(panel)
        layout = QVBoxLayout(panel)
        self.model_box = QComboBox()
        self.model_box.addItems(list(predictors))
        self.service = PredictionService(predictors[self.model_box.currentText()])
        model_form = QFormLayout()
        model_form.addRow("Модель", self.model_box)
        layout.addLayout(model_form)
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)
        form_page = QWidget()
        form = QFormLayout(form_page)
        self.fields = []
        for label, example in self.FEATURES:
            field = QLineEdit()
            field.setPlaceholderText(f"Например, {example}")
            field.returnPressed.connect(self.on_predict_clicked)
            form.addRow(label, field)
            self.fields.append(field)
        self.tabs.addTab(form_page, "По полям")

        line_page = QWidget()
        line_layout = QVBoxLayout(line_page)
        order = QLabel("\n".join(
            f"{i}. {label}" for i, (label, _) in enumerate(self.FEATURES, start=1)
        ))
        line_layout.addWidget(order)
        self.features_input = QLineEdit()
        self.features_input.setPlaceholderText("Признаки через запятую")
        line_layout.addWidget(self.features_input)
        line_layout.addStretch()
        self.tabs.addTab(line_page, "Одной строкой")
        self.predict_button = QPushButton("Предсказать")
        self.clear_button = QPushButton("Очистить")
        self.result_label = QLabel(self.INITIAL_RESULT)
        self.result_label.setWordWrap(True)

        layout.addWidget(self.predict_button)
        layout.addWidget(self.clear_button)
        layout.addWidget(self.result_label)
        self.probability_bar = QProgressBar()
        self.probability_bar.setRange(0, 100)
        self.probability_bar.setFormat("Вероятность предсказанного класса: %p%")
        layout.addWidget(self.probability_bar)
        self.probability_bar.hide()

        self.model_box.currentIndexChanged.connect(self.on_model_changed)
        self.predict_button.clicked.connect(self.on_predict_clicked)
        self.features_input.returnPressed.connect(self.on_predict_clicked)
        self.clear_button.clicked.connect(self.on_clear_clicked)
        self.tabs.currentChanged.connect(self.reset_result)

    @Slot()
    def reset_result(self):
        self.result_label.setText(self.INITIAL_RESULT)
        self.probability_bar.hide()

    @Slot(int)
    def on_model_changed(self, index):
        self.service.predictor = self.predictors[self.model_box.itemText(index)]
        self.reset_result()

    @Slot(float)
    def on_probability(self, probability):
        self.probability_bar.setValue(round(probability * 100))
        self.probability_bar.show()

    @Slot()
    def on_predict_clicked(self):
        if self.worker is not None:
            return
        try:
            text = self.input_text()
        except ValueError as error:
            self.on_error(str(error))
            return

        self.worker = PredictWorker(self.service, text, self)
        self.probability_bar.hide()
        self.worker.probability_ready.connect(self.on_probability)
        self.worker.finished_ok.connect(self.on_success)
        self.worker.failed.connect(self.on_error)
        self.worker.finished.connect(self.on_worker_finished)
        self.worker.finished.connect(self.worker.deleteLater)
        self.set_inputs_enabled(False)
        self.result_label.setText("Вычисление...")
        self.worker.start()

    def input_text(self):
        if self.tabs.currentIndex() == 1:
            return self.features_input.text()

        values = []
        for (label, _), field in zip(self.FEATURES, self.fields):
            value = field.text().strip().replace(",", ".")
            try:
                float(value)
            except ValueError:
                field.setFocus()
                raise ValueError(f"Введите число в поле «{label}».") from None
            values.append(value)
        return ", ".join(values)

    def set_inputs_enabled(self, enabled: bool):
        self.model_box.setEnabled(enabled)
        self.tabs.setEnabled(enabled)
        self.predict_button.setEnabled(enabled)
        self.clear_button.setEnabled(enabled)

    @Slot(str)
    def on_success(self, result):
        self.result_label.setText(result)

    @Slot(str)
    def on_error(self, message):
        self.probability_bar.hide()
        self.result_label.setText(message)

    @Slot()
    def on_worker_finished(self):
        self.worker = None
        self.set_inputs_enabled(True)
        if self.close_requested:
            self.close()

    def closeEvent(self, event):
        if self.worker is not None:
            self.close_requested = True
            event.ignore()
        else:
            super().closeEvent(event)

    @Slot()
    def on_clear_clicked(self):
        for field in self.fields:
            field.clear()
        self.features_input.clear()
        self.reset_result()
        active_input = self.fields[0] if self.tabs.currentIndex() == 0 else self.features_input
        active_input.setFocus()
