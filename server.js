require('dotenv').config();
const express = require('express');
const axios = require('axios');

const app = express();
const PORT = process.env.PORT || 3000;

// Ruta para obtener los hubs de Autodesk Forge
app.get('/hubs', async (req, res) => {
    try {
        const token = process.env.FORGE_ACCESS_TOKEN; // Carga el token de las variables de entorno
        const response = await axios.get("https://developer.api.autodesk.com/project/v1/hubs", {
            headers: { Authorization: `Bearer ${token}` }
        });
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Ruta para crear un bucket en Forge
app.post('/create-bucket', async (req, res) => {
    try {
        const token = process.env.FORGE_ACCESS_TOKEN;
        const bucketKey = "mi-bucket"; // El nombre del bucket
        const policyKey = "transient"; // Política del bucket

        const response = await axios.post("https://developer.api.autodesk.com/oss/v2/buckets", {
            bucketKey: bucketKey,
            policyKey: policyKey
        }, {
            headers: {
                Authorization: `Bearer ${token}`,
                "Content-Type": "application/json"
            }
        });

        res.json(response.data); // Devuelve la respuesta de la creación del bucket
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Iniciar el servidor
app.listen(PORT, () => {
    console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
