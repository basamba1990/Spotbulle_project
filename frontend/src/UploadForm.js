import React, { useState } from 'react';
import axios from 'axios';

function UploadForm() {
    const [file, setFile] = useState(null);
    const [transcription, setTranscription] = useState('');
    const [category, setCategory] = useState('');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (!file) {
            setError('Veuillez sélectionner un fichier.');
            return;
        }

        setError('');
        setLoading(true);

        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await axios.post('http://localhost:8090/upload', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });

            setTranscription(response.data.transcription);
            setCategory(response.data.category);
        } catch (error) {
            setError(error.response?.data?.error || 'Une erreur est survenue.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div style={{ textAlign: 'center', marginTop: '20px' }}>
            <h1>Uploader une vidéo</h1>
            <form onSubmit={handleSubmit}>
                <input type="file" name="file" onChange={handleFileChange} required />
                <button type="submit" disabled={loading}>
                    {loading ? 'Envoi en cours...' : 'Envoyer'}
                </button>
            </form>

            {error && <p style={{ color: 'red' }}>{error}</p>}

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
