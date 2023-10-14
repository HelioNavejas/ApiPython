from flask import Blueprint, request
from models.Helado import Helado
from controllers.controller import new, view

icecream = Blueprint('icecream', __name__)

@icecream.route("/new", methods=['POST'])
def add_iceCream():
    name = request.form['name']
    flavor = request.form['flavor']
    newHelado = Helado(name, flavor)
    new(newHelado)
    return name + " " + flavor

@icecream.route("/view")
def view_iceCream():
    viewHelado = view()
    results = ""
    for helado in viewHelado:
        print (helado)
        results = results+str(helado)+"\n"
    return results
