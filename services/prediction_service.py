from collections.abc import Callable
from math import isfinite

from ml.predictor import Predictor


class PredictionService:
    def __init__(self, predictor: Predictor):
        self.predictor = predictor

    def run(self, text: str, on_probability: Callable[[float], None] | None = None) -> str:
        if not text.strip():
            raise ValueError("Введите признаки через запятую.")
        try:
            features = [float(value) for value in text.split(",")]
        except ValueError as error:
            raise ValueError("Введите числа через запятую, например 20, 96019, 23421, 24, 0, 1, 14.") from error
        if not all(isfinite(value) for value in features):
            raise ValueError("Все признаки должны быть конечными числами.")

        result = self.predictor.predict(features)
        if on_probability is not None and "proba" in result:
            on_probability(result["proba"])
        return {0: "Нет дефолта", 1: "Дефолт"}[result["prediction"]]
