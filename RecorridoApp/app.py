from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)  # permite solicitudes desde otros orígenes (como tu app Expo)

# Conexión a PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="mi_basededatos",
    user="mi_usuario",
    password="mi_contraseña"
)

@app.route('/api/usuarios')
def get_usuarios():
    cur = conn.cursor()
    cur.execute('SELECT id, nombre FROM usuarios')
    rows = cur.fetchall()
    cur.close()
    return jsonify([{"id": r[0], "nombre": r[1]} for r in rows])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

