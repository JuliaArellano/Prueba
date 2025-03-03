require('dotenv').config();
const axios = require('axios');

// Obtener el Client ID y Client Secret del archivo .env
const clientId = process.env.FORGE_CLIENT_ID;
const clientSecret = process.env.FORGE_CLIENT_SECRET;

// Función para obtener el access token
const getAccessToken = async () => {
  try {
    const response = await axios.post(
      'https://developer.api.autodesk.com/authentication/v1/authenticate',
      new URLSearchParams({
        client_id: clientId,
        client_secret: clientSecret,
        grant_type: 'client_credentials',
        scope: 'data:read data:write'
      }),
      { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } }
    );

    // Extraer el access token de la respuesta
    const accessToken = response.data.access_token;
    console.log('Token de acceso obtenido:', accessToken);

    return accessToken;
  } catch (error) {
    console.error('Error al obtener el token:', error);
  }
};

// Llamar a la función para obtener el token
getAccessToken();
