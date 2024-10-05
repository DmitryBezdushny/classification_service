import pandas as pd
import pickle
from src.config_parser import CONFIG


class Model:

    def __init__(self):
        self.model = pickle.load(open(CONFIG['model_path'], "rb"))

    def predict(self, request):
        request = {k: [v] for k, v in request.items()}
        feature_vector = pd.DataFrame(request)
        score = self.model.predict(feature_vector)[0]
        return {"score": float(score)}