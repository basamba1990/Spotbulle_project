import React, { useState } from "react";
import API_BASE_URL from "./config"; // Import de l'URL de l'API

function UploadForm() {
    const [file, setFile] = useState(null);
    const [transcription, setTranscription] = useState('');
    const [category, setCategory] = useState('');

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append("file", file);

        try {
            const response = await fetch(`${API_BASE_URL}/upload`, {
                method: "POST",
                body: formData,
            });

            if (!response.ok) {
                throw new Error("Erreur lors de l'upload");
            }

            const result = await response.json();
            setTranscription(result.transcription || "Pas de transcription trouvée");
            setCategory(result.category || "Pas de catégorie détectée");
        } catch (error) {
            console.error("Erreur:", error);
        }
    };

    return (
        <div>
            <h1>Uploader une vidéo</h1>
            <form onSubmit={handleSubmit}>
                <input type="file" name="file" onChange={handleFileChange} required />
                <button type="submit">Envoyer</button>
            </form>
            {transcription && (
                <div>
                    <h2>Transcription :</h2>
                    <p>{transcription}</p>
                </div>
            )}
            {category && (
                <div>
                    <h2>Catégorie :</h2>
                    <p>{category}</p>
                </div>
            )}
        </div>
    );
}

export default UploadForm;
