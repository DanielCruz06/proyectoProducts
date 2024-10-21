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

# Crear la tabla de productos al iniciar el microservicio
def create_product_table():
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id UUID PRIMARY KEY,
                name TEXT NOT NULL,
                price DECIMAL NOT NULL
            )
        ''')
        conn.commit()
    conn.close()

@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    product_id = str(uuid.uuid4())
    name = data.get('name')
    price = data.get('price')

    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute('''
                INSERT INTO products (id, name, price)
                VALUES (%s, %s, %s)
            ''', (product_id, name, price))
            conn.commit()
        conn.close()
        return jsonify({"message": "Product created", "product_id": product_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/products', methods=['GET'])
def get_products():
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM products')
        products = cursor.fetchall()
    conn.close()
    return jsonify(products), 200

if __name__ == '__main__':
    create_product_table()  # Crear la tabla al iniciar el servicio
    app.run(host='0.0.0.0', port=5001)

