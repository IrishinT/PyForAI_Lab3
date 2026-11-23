import sys

from PySide6.QtWidgets import QApplication

from config import LOGISTIC_MODEL_PATH, MODEL_PATH
from desktop.main_window import MainWindow
from ml.predictor import Predictor


def main():
    app = QApplication(sys.argv)
    window = MainWindow({
        "Нейросеть": Predictor(MODEL_PATH),
        "Логистическая регрессия": Predictor(LOGISTIC_MODEL_PATH),
    })
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
