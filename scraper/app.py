import requests
from flask import Flask

app = Flask(__name__)

OFF_SEARCH_URL = "https://world.openfoodfacts.net/api/v2/product/3017624010701?fields=product_name,nutriscore_data"
TIMEOUT = 10
CACHE_SIZE = 128


@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"


@app.route("/protein/<item>")
def get_protein(item):
    return f"<h1>{item}</h1>"


@app.route("/nutella")
def get_nutella():
    result = requests.get(OFF_SEARCH_URL)
    print("Hello Dude")
    print(result)
    return f"<p>{str(result)}</p>"
