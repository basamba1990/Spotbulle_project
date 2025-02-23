import whisper

def transcribe_video(video_path: str) -> str:
    """Utilise Whisper pour transcrire un fichier audio/vidéo en texte."""
    model = whisper.load_model("base")
    result = model.transcribe(video_path)
    return result["text"]
