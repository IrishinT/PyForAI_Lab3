from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow

from desktop.ui_main_window import Ui_MainWindow
from desktop.worker import PredictWorker
from ml.predictor import Predictor
from services.prediction_service import PredictionService


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, predictors: dict[str, Predictor]):
        super().__init__()
        self.predictors = predictors
        self.worker = None
        self.close_requested = False
        self.setupUi(self)
        self.initial_result = self.result_label.text()
        self.model_box.addItems(list(predictors))
        self.service = PredictionService(predictors[self.model_box.currentText()])
        self.fields = (
            self.age_input, self.income_input, self.amount_input, self.term_input,
            self.loans_input, self.late_input, self.employment_input,
        )
        for field in self.fields:
            field.returnPressed.connect(self.on_predict_clicked)
        self.probability_bar.hide()

        self.model_box.currentIndexChanged.connect(self.on_model_changed)
        self.predict_button.clicked.connect(self.on_predict_clicked)
        self.features_input.returnPressed.connect(self.on_predict_clicked)
        self.clear_button.clicked.connect(self.on_clear_clicked)
        self.tabs.currentChanged.connect(self.reset_result)

    @Slot()
    def reset_result(self):
        self.result_label.setText(self.initial_result)
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
        for field in self.fields:
            value = field.text().strip().replace(",", ".")
            try:
                float(value)
            except ValueError:
                field.setFocus()
                label = self.feature_form.labelForField(field).text()
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
