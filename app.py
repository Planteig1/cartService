from flask import Flask, jsonify, request, make_response
import requests
"""
Cart Service:

Håndterer brugernes indkøbskurve.

Tilbyder funktioner til at tilføje, fjerne og opdatere varer i kurven.
"""

app = Flask(__name__)

cart_db = []

#Show items in cart - GET
@app.route('/cart', methods = ["GET"])
def get_cart_items():
    return jsonify(cart_db)

#Add item to cart - POST
@app.route('/cart', methods = ["POST"])
def add_item_to_cart():
    data = request.json
    item_id = data.get("id")

    #Add the item - Using data from dummyjson ( Should be from another microservice) could add error handling
    response = requests.get(f"https://dummyjson.com/products/{item_id}")
    cart_db.append(response.json())

    return "item added successfully", 201

#Remove item from cart - POST
@app.route('/cart', methods = ["DELETE"])
def remove_item_from_cart():
    data = request.json
    item_id = data.get("id")

    # Finds the index of the product - could add error handling
    index = next((i for i, product in enumerate(cart_db) if product["id"] == item_id), None)   
    # Remove the product from the list 
    cart_db.pop(index)
    return "Item deleted successfully", 201

app.run(debug=True, host="0.0.0.0")

