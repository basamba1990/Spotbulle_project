from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from models.transcriber import transcribe_video
from models.classifier import classify_pitch

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "Aucun fichier reçu"}), 400

    file = request.files["file"]
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    try:
        # Transcription
        transcription = transcribe_video(file_path)

        # Classification
        category = classify_pitch(transcription)

        return jsonify({"transcription": transcription, "category": category})
    
    except Exception as e:
        return jsonify({"error": f"Erreur lors du traitement : {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090, debug=True)
