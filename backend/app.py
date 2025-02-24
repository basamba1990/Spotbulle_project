from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Autorise toutes les origines

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {'mp4', 'mov', 'avi', 'mkv'}  # Extensions autorisées pour les vidéos

# Vérifier si le fichier a une extension valide
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "Aucun fichier reçu"}), 400

    file = request.files["file"]

    # Vérifier si le fichier est autorisé
    if not allowed_file(file.filename):
        return jsonify({"error": "Extension de fichier non autorisée"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Traitement supplémentaire si nécessaire
    # Exemple: Lancer une fonction de transcription ou de classification sur le fichier
    # transcription = transcribe_video(file_path)
    # category = classify_pitch(transcription)

    return jsonify({
        "message": "Fichier uploadé avec succès",
        "file_name": file.filename,
        "file_path": file_path,
        "file_size": os.path.getsize(file_path),  # Taille du fichier en octets
        # "transcription": transcription,  # Si vous ajoutez une fonction de transcription
        # "category": category  # Si vous ajoutez une fonction de classification
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
