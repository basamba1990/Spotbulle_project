import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

# Charger le modèle pré-entraîné (à créer séparément)
model = joblib.load("models/pitch_classifier.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

def classify_pitch(text: str) -> str:
    """Classifie un pitch en fonction de son contenu textuel."""
    features = vectorizer.transform([text])
    category = model.predict(features)
    return category[0]
