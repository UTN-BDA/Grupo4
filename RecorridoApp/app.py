# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import os
from pathlib import Path

from dotenv import load_dotenv
env_path = Path(__file__).resolve().parent.parent / 'docker-postgresql' / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
CORS(app)  # Permite solicitudes desde el frontend

# Configurar conexión a PostgreSQL
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    port=os.getenv("DB_PORT")
)

@app.route("/api/search_trips", methods=["GET"])
def search_trips():
    origin = request.args.get("origin")
    destination = request.args.get("destination")

    if not origin or not destination:
        return jsonify({"error": "Missing origin or destination"}), 400

    try:
        cur = conn.cursor()
        cur.execute('''
            SELECT id, origin, destination, company, price, 
                   to_char(departure_time, 'HH24:MI') AS departure_time, 
                   to_char(arrival_time, 'HH24:MI') AS arrival_time
            FROM trips
            WHERE LOWER(origin) = LOWER(%s) AND LOWER(destination) = LOWER(%s)
        ''', (origin, destination))

        rows = cur.fetchall()
        trips = [
            {
                "id": row[0],
                "origin": row[1],
                "destination": row[2],
                "company": row[3],
                "price": row[4],
                "departure_time": row[5],
                "arrival_time": row[6],
            }
            for row in rows
        ]
        cur.close()
        return jsonify(trips)

    except Exception as e:
        print("Error al consultar la base de datos:", e)
        return jsonify({"error": "Database error"}), 500

if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=5000, debug=True)
