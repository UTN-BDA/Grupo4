const API_URL = 'http://localhost:5000/api/v1/viajes';

async function fetchViajes() {
  try {
    console.log(`Consultando la API en: ${API_URL}`);
    const response = await fetch(API_URL);

    if (!response.ok) {
      throw new Error(`HTTP Error ${response.status}`);
    }

    const json = await response.json();

    if (json.success) {
      console.log("✅ Datos recibidos correctamente:\n");
      console.dir(json.data, { depth: null });
    } else {
      console.error("❌ Error en la respuesta:", json.error || 'Respuesta no exitosa');
    }

  } catch (error) {
    console.error("❌ Error al consultar la API:", error.message);
  }
}

fetchViajes();
