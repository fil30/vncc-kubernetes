from flask import Flask, jsonify, request, render_template, make_response
from models import list_shop
from database import get_session
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins='*')


@app.route('/add_product', methods=['POST'])
def add_product():
    product_name = request.form.get('product')
    amount = request.form.get('quantita')
    price = request.form.get('prezzo')

    # Aggiungo il prodotto al db.
    if product_name and amount and price:
        with get_session() as db:
            new_product = list_shop(
                product_name=product_name, amount=amount, price=price)
            db.add(new_product)
            db.commit()

            response = make_response(jsonify(new_product))
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")