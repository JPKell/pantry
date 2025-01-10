from flask import Blueprint, json, redirect, request, session, url_for, render_template

from modules.ingredients import Ingredient
from modules.market      import Market   

from app import db, chef, pantry

bp = Blueprint('market', __name__) 

@bp.route("/markets")
def markets():
    return render_template("index.html", 
                           body =" market_table()", 
                           activeNav = "markets")
