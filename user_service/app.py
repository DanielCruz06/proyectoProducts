from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
import uuid
import os

app = Flask(__name__)

# Configuración de la base de datos a través de una variable de entorno
DATABASE_URL = os.environ.get('DATABASE_URL')

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
    return conn

# Crear la tabla de usuarios al iniciar el microservicio
def create_user_table():
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id UUID PRIMARY KEY,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()
    conn.close()

@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    user_id = str(uuid.uuid4())
    username = data.get('username')
    password = data.get('password')

    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute('''
                INSERT INTO users (id, username, password)
                VALUES (%s, %s, %s)
            ''', (user_id, username, password))
            conn.commit()
        conn.close()
        return jsonify({"message": "User registered successfully", "user_id": user_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute('SELECT id, password FROM users WHERE username = %s', (username,))
        user = cursor.fetchone()
    
    conn.close()

    if user and user['password'] == password:
        return jsonify({"message": "Login successful", "user_id": user['id']}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

if __name__ == '__main__':
    create_user_table()  # Crear la tabla al iniciar el servicio
    app.run(host='0.0.0.0', port=5000)

