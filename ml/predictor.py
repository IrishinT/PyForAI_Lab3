from pathlib import Path

import joblib
import pandas as pd


class Predictor:
    def __init__(self, model_path: Path):
        self.model = joblib.load(model_path)

    def predict(self, features: list[float]) -> dict:
        expected = self.model.n_features_in_
        if len(features) != expected:
            raise ValueError(f"Ожидается {expected} признаков, получено {len(features)}.")

        sample = pd.DataFrame([features], columns=self.model.feature_names_in_)
        prediction = int(self.model.predict(sample)[0])
        result = {"prediction": prediction}
        if hasattr(self.model, "predict_proba"):
            index = self.model.classes_.tolist().index(prediction)
            result["proba"] = float(self.model.predict_proba(sample)[0, index])
        return result
