import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


from config import MODEL_PATH, ROOT


def main():
    data = pd.read_csv(ROOT / "data" / "credit_scoring.csv")
    target = data.pop("default")
    x_train, x_test, y_train, y_test = train_test_split(
        data, target, test_size=0.2, random_state=42, stratify=target
    )
    model = Pipeline([
        ("scaler", StandardScaler()),
        ("mlp", MLPClassifier(
            hidden_layer_sizes=(64, 32), max_iter=3000, random_state=42
        )),
    ])
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    probabilities = model.predict_proba(x_test)

    MODEL_PATH.parent.mkdir(exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    restored = joblib.load(MODEL_PATH)
    np.testing.assert_array_equal(restored.predict(x_test), predictions)
    np.testing.assert_array_equal(restored.predict_proba(x_test), probabilities)

    print(f"Train/test: {len(x_train)}/{len(x_test)}")
    print(f"Accuracy: {accuracy_score(y_test, predictions):.4f}")
    print(f"F1 (default=1): {f1_score(y_test, predictions):.4f}")
    print("Input:", ", ".join(f"{value:g}" for value in x_test.iloc[0]))
    print("Prediction:", predictions[0])
    print("Probabilities:", dict(zip(model.classes_.tolist(), probabilities[0].tolist())))


if __name__ == "__main__":
    main()
