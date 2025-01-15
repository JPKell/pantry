from flask import Blueprint, json, redirect, request, session, url_for, render_template

from modules.ingredients import Ingredient
from modules.market      import Market   

from pages.market.list import market_list

from app import db, chef, pantry, nav

bp = Blueprint('market', __name__) 

@bp.route("/markets/<string:name>")
@bp.route("/markets")
def markets(name:str=None):
    if name:
        return render_template("index.html", 
                               body = market_list(name), 
                               nav=nav)
    else:
        return render_template("index.html", 
                                body =" market_table()", 
                                nav=nav)
