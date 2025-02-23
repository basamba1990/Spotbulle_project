import os
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

model_path = "models/pitch_classifier.pkl"
vectorizer_path = "models/vectorizer.pkl"

if not os.path.exists(model_path) or not os.path.exists(vectorizer_path):
    raise FileNotFoundError("Le modèle ou le vectorizer est introuvable. Vérifiez les fichiers.")

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

def classify_pitch(text: str) -> str:
    """Classifie un pitch en fonction de son contenu textuel."""
    features = vectorizer.transform([text])
    category = model.predict(features)
    return category[0]
