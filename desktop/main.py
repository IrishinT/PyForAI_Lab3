import sys

from PySide6.QtWidgets import QApplication

from config import MODEL_PATH
from desktop.main_window import MainWindow
from ml.predictor import Predictor
from services.prediction_service import PredictionService


def main():
    app = QApplication(sys.argv)
    window = MainWindow(PredictionService(Predictor(MODEL_PATH)))
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
