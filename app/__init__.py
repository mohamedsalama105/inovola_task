from flask import Flask , request
import json
from .database_handler import coffee_db
app = Flask(__name__)
coffee_database=coffee_db()
app.config["DEBUG"] = True



@app.route("/coffee_machine", methods=["POST"])
def Coffee_machines():
    filter = request.get_json()
    products = coffee_database.get_products("coffee_machines",filter)
    return json.dumps(products)

@app.route("/coffee_pod", methods=["POST"])
def Coffee_pods():
    filter = request.get_json()
    products = coffee_database.get_products("coffee_pods",filter)
    return json.dumps(products)

