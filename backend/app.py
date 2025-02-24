from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys

# Ajout du chemin du dossier backend pour éviter les problèmes d'importation
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

try:
    from models.transcriber import transcribe_video
    print("✅ Importation de transcriber OK")
except ImportError as e:
    print(f"❌ Erreur lors de l'importation de transcriber: {e}")
    transcribe_video = None

try:
    from models.classifier import classify_pitch
    print("✅ Importation de classifier OK")
except ImportError as e:
    print(f"❌ Erreur lors de l'importation de classifier: {e}")
    classify_pitch = None

# Initialisation de l'application Flask
app = Flask(__name__)

# Configuration de CORS
CORS(app, resources={r"/upload": {"origins": "http://localhost:3000"}})

# Définition du dossier de stockage des fichiers uploadés
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.chmod(UPLOAD_FOLDER, 0o777)  # S'assurer que le dossier est accessible

@app.route("/", methods=["GET"])
def home():
    """ Vérifier si le serveur fonctionne """
    return jsonify({"message": "API en ligne", "routes": [rule.rule for rule in app.url_map.iter_rules()]})

@app.route("/upload", methods=["POST"])
def upload_file():
    """ Endpoint pour uploader un fichier et le traiter """
    if "file" not in request.files:
        return jsonify({"error": "Aucun fichier reçu"}), 400

    file = request.files["file"]
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    try:
        if transcribe_video is None or classify_pitch is None:
            return jsonify({"error": "Modules non disponibles"}), 500

        # Transcription du fichier vidéo
        transcription = transcribe_video(file_path)

        # Classification du texte transcrit
        category = classify_pitch(transcription)

        return jsonify({"transcription": transcription, "category": category})
    
    except Exception as e:
        return jsonify({"error": f"Erreur lors du traitement : {str(e)}"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8090))  # Adaptation pour le déploiement
    app.run(host="0.0.0.0", port=port, debug=True)
