from pathlib import Path


ROOT = Path(__file__).resolve().parent
MODEL_PATH = ROOT / "models" / "credit_mlp.joblib"
LOGISTIC_MODEL_PATH = ROOT / "models" / "credit_logistic.joblib"
