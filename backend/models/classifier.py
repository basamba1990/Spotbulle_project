import os import joblib from sklearn.feature_extraction.text import TfidfVectorizer from sklearn.naive_bayes import MultinomialNB

Définition des chemins

model_path = "models/pitch_classifier.pkl" vectorizer_path = "models/vectorizer.pkl"

Données d'entraînement

texts = [ "Spot Bulle et GENUP2050 sont des outils par et pour la jeunesse...", "Le projet GENUP2050 a pour objectif de propulser une synergie...", "Création de Spot Bulle en France pour accompagner les jeunes...", "GENUP2050 cherche à lever des fonds pour développer Spot Bulle...", "Spot Bulle aide à l'identification des talents jeunes...", "Le projet Spot Bulle inclut une expansion en Afrique...", "La méthode Funny Color et la formation NO CODE permettent...", "Spot Bulle développe un modèle économique durable...", "Spot Bulle favorise l'entrepreneuriat à impact social...", "L'initiative Spot Bulle vise à créer une plateforme incontournable..." ] labels = [ "Plateforme éducative", "Mentorat et Synergie", "Détection de talents", "Levée de fonds et IA", "Formation personnalisée", "Expansion internationale", "Emploi et formation", "Modèle économique durable", "Entrepreneuriat social", "Plateforme incontournable" ]

Vérification et création du modèle si absent

if not os.path.exists(model_path) or not os.path.exists(vectorizer_path): os.makedirs("models", exist_ok=True) vectorizer = TfidfVectorizer() X_train = vectorizer.fit_transform(texts) model = MultinomialNB() model.fit(X_train, labels) joblib.dump(model, model_path) joblib.dump(vectorizer, vectorizer_path) else: model = joblib.load(model_path) vectorizer = joblib.load(vectorizer_path)

def classify_pitch(text: str) -> str: """Classifie un pitch en fonction de son contenu textuel.""" features = vectorizer.transform([text]) category = model.predict(features) return category[0]

