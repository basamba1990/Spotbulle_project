import torch
from whisper import load_model, transcribe

def transcribe_video(video_path: str) -> str:
    """
    Transcrit l'audio d'une vidéo en texte en utilisant Whisper.
    
    Parameters
    ----------
    video_path : str
        Chemin vers le fichier vidéo.
    
    Returns
    -------
    str
        Transcription textuelle de l'audio.
    """
    # Charger le modèle Whisper
    model = load_model("base")  # Vous pouvez utiliser "small", "medium", etc.

    # Extraire l'audio et transcrire
    result = transcribe(model, video_path)
    return result["text"]
