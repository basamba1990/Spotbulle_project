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
    try:
        if "file" not in request.files:
            return jsonify({"error": "Aucun fichier reçu"}), 400

        file = request.files["file"]

        # Vérifier si le fichier est autorisé
        if not allowed_file(file.filename):
            return jsonify({"error": "Extension de fichier non autorisée"}), 400

        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        return jsonify({
            "message": "Fichier uploadé avec succès",
            "file_name": file.filename,
            "file_path": file_path,
            "file_size": os.path.getsize(file_path),  # Taille du fichier en octets
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Récupérer le port à partir de la variable d'environnement ou utiliser 8090 par défaut
    port = int(os.environ.get("PORT", 8090))
    app.run(debug=True, host="0.0.0.0", port=port)
