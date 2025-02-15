from flask import Blueprint, json, redirect, request, session, url_for, render_template

from modules.ingredients import Ingredient
from modules.market      import Market   

from pages.market.list import market_list
from pages.market.compare import market_compare

from app import db, chef, pantry, nav

bp = Blueprint('market', __name__) 

@bp.route("/markets/<string:name>")
@bp.route("/markets")
def markets(name:str=None):
    if name == 'compare':
        return render_template("index.html", 
                               body = market_compare(), 
                               nav=nav)       
    if name:
        return render_template("index.html", 
                               body = market_list(name), 
                               nav=nav)
    else:
        return render_template("index.html", 
                                body =" market_table()", 
                                nav=nav)
