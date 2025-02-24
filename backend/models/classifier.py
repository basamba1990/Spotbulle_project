import os import joblib from sklearn.feature_extraction.text import TfidfVectorizer from sklearn.naive_bayes import MultinomialNB from sklearn.metrics import accuracy_score

Définition des chemins

MODEL_DIR = "models" MODEL_PATH = os.path.join(MODEL_DIR, "pitch_classifier.pkl") VECTORIZER_PATH = os.path.join(MODEL_DIR, "vectorizer.pkl")

Création du répertoire si nécessaire

os.makedirs(MODEL_DIR, exist_ok=True)

Données d'entraînement

texts = [ "Spot Bulle et GENUP2050 sont des outils par et pour la jeunesse...", "Le projet GENUP2050 a pour objectif de propulser une synergie...", "Création de Spot Bulle en France pour accompagner les jeunes...", "GENUP2050 cherche à lever des fonds pour développer Spot Bulle...", "Spot Bulle aide à l'identification des talents jeunes...", "Le projet Spot Bulle inclut une expansion en Afrique...", "La méthode Funny Color et la formation NO CODE permettent...", "Spot Bulle développe un modèle économique durable...", "Spot Bulle favorise l'entrepreneuriat à impact social...", "L'initiative Spot Bulle vise à créer une plateforme incontournable..." ] labels = [ "Plateforme éducative", "Mentorat et Synergie", "Détection de talents", "Levée de fonds et IA", "Formation personnalisée", "Expansion internationale", "Emploi et formation", "Modèle économique durable", "Entrepreneuriat social", "Plateforme incontournable" ]

Vérification et chargement du modèle

if os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH): model = joblib.load(MODEL_PATH) vectorizer = joblib.load(VECTORIZER_PATH) print("Modèle chargé avec succès.") else: print("Modèle introuvable, création d'un nouveau modèle...") vectorizer = TfidfVectorizer() X_train = vectorizer.fit_transform(texts) model = MultinomialNB() model.fit(X_train, labels) joblib.dump(model, MODEL_PATH) joblib.dump(vectorizer, VECTORIZER_PATH) print("Modèle entraîné et sauvegardé.")

Fonction de classification

def classify_pitch(text: str) -> str: """Classifie un pitch en fonction de son contenu textuel.""" features = vectorizer.transform([text]) category = model.predict(features) return category[0]

Évaluation du modèle

def evaluate_model(): """Évalue la précision du modèle sur un sous-ensemble de test.""" X_test = vectorizer.transform(texts)  # Réutilisation des textes d'entraînement (améliorable) y_pred = model.predict(X_test) accuracy = accuracy_score(labels, y_pred) print(f"Précision du modèle : {accuracy:.2f}")

evaluate_model()

Interface utilisateur

def interactive_classification(): """Interface CLI pour tester la classification.""" while True: text = input("Entrez un pitch (ou 'exit' pour quitter) : ") if text.lower() == "exit": break print("Catégorie prédite :", classify_pitch(text))

Activer l'interface utilisateur

if name == "main": interactive_classification()

