from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QFormLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QTabWidget,
    QVBoxLayout, QWidget,
)

from desktop.worker import PredictWorker
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

    def __init__(self, service: PredictionService):
        super().__init__()
        self.service = service
        self.worker = None
        self.close_requested = False
        self.setWindowTitle("Кредитный скоринг")
        self.resize(500, 390)

        panel = QWidget()
        self.setCentralWidget(panel)
        layout = QVBoxLayout(panel)
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

        self.predict_button.clicked.connect(self.on_predict_clicked)
        self.features_input.returnPressed.connect(self.on_predict_clicked)
        self.clear_button.clicked.connect(self.on_clear_clicked)
        self.tabs.currentChanged.connect(self.reset_result)

    @Slot()
    def reset_result(self):
        self.result_label.setText(self.INITIAL_RESULT)

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
        self.tabs.setEnabled(enabled)
        self.predict_button.setEnabled(enabled)
        self.clear_button.setEnabled(enabled)

    @Slot(str)
    def on_success(self, result):
        self.result_label.setText(result)

    @Slot(str)
    def on_error(self, message):
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
