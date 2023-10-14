from flask import Flask
from routes.iceCream import icecream

app = Flask(__name__)

app.register_blueprint(icecream)