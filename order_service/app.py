from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# Simulación de base de datos de órdenes en memoria
orders = {}

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    order_id = str(uuid.uuid4())
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    orders[order_id] = {"product_id": product_id, "quantity": quantity}
    return jsonify({"message": "Order created", "order_id": order_id}), 201

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

