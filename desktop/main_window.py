from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QFormLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QTabWidget,
    QVBoxLayout, QWidget,
)

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
        try:
            if self.tabs.currentIndex() == 0:
                values = []
                for (label, _), field in zip(self.FEATURES, self.fields):
                    value = field.text().strip().replace(",", ".")
                    try:
                        float(value)
                    except ValueError:
                        field.setFocus()
                        raise ValueError(f"Введите число в поле «{label}».") from None
                    values.append(value)
                text = ", ".join(values)
            else:
                text = self.features_input.text()
            result = self.service.run(text)
        except ValueError as error:
            result = str(error)
        self.result_label.setText(result)

    @Slot()
    def on_clear_clicked(self):
        for field in self.fields:
            field.clear()
        self.features_input.clear()
        self.reset_result()
        active_input = self.fields[0] if self.tabs.currentIndex() == 0 else self.features_input
        active_input.setFocus()
