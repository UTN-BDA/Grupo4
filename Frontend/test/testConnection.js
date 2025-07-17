// Para poder usar 'import' en un script de Node.js, asegúrate de que tu
// package.json contenga la línea: "type": "module"
// O, alternativamente, puedes cambiar el nombre del archivo a 'testConnection.mjs'
import fetch from 'node-fetch';

// --- ¡IMPORTANTE! ---
// Reemplaza esta URL con la dirección IP de tu servidor Flask.
// Si el servidor se ejecuta en la misma máquina, 'localhost' debería funcionar.
const origen = 'San Rafael';
const destino = 'Mendoza Capital';
const API_URL = `http://localhost:5000//api/v1/viajes?origen=${origen}&destino=${destino}`;


/**
 * Función asíncrona para probar la conexión con el backend de Flask.
 */
async function testApiConnection() {
  console.log('================================================');
  console.log('    INICIANDO PRUEBA DE CONEXIÓN AL BACKEND     ');
  console.log('================================================');
  console.log(`\nIntentando conectar con: ${API_URL}\n`);

  try {
    // Realizamos la petición a la API
    const response = await fetch(API_URL);

    // Verificamos si la respuesta HTTP no fue exitosa (ej: 404, 500)
    if (!response.ok) {
      const errorBody = await response.text(); // Intentamos leer el cuerpo del error
      throw new Error(`Error en la respuesta del servidor (HTTP ${response.status}): ${errorBody}`);
    }

    // Si la respuesta es exitosa, la convertimos a JSON
    const data = await response.json();

    // Verificamos el campo 'success' de nuestra respuesta JSON personalizada
    if (data.success) {
      console.log('✅ --- ¡CONEXIÓN EXITOSA! --- ✅');
      console.log(`\nSe recibieron un total de ${data.total} viaje(s).`);
      
      if (data.total > 0) {
        console.log('\n--- DATOS RECIBIDOS ---');
        // Usamos JSON.stringify con formato para que la salida sea legible
        console.log(JSON.stringify(data.data, null, 2));
        console.log('\n-----------------------\n');
        console.log('La estructura de los datos es correcta. ¡Integración validada!');
      } else {
        console.log('\nLa conexión fue exitosa, pero la base de datos no devolvió resultados.');
      }
    } else {
      // Si el campo 'success' es false
      throw new Error(`El servidor respondió con un error de aplicación: ${data.error}`);
    }

  } catch (error) {
    console.error('\n❌ --- FALLÓ LA PRUEBA DE CONEXIÓN --- ❌');
    console.error('\nHa ocurrido un error:', error.message);
    console.error('\n--- POSIBLES SOLUCIONES ---');
    console.error('1. Asegúrate de que tu servidor Flask esté en ejecución.');
    console.error('2. Revisa que la dirección IP y el puerto en la variable API_URL sean correctos.');
    console.error('3. Si ejecutas este script en una máquina diferente al servidor, verifica que un firewall no esté bloqueando la conexión.');
    console.error('4. Confirma que el endpoint `/viajes` no requiere parámetros obligatorios para una petición GET general.');
  } finally {
    console.log('\n================================================');
    console.log('            PRUEBA DE CONEXIÓN FINALIZADA         ');
    console.log('================================================');
  }
}

// Ejecutamos la función de prueba
testApiConnection();
