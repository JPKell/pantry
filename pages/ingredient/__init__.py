from flask import Blueprint, json, redirect, request, session, url_for, render_template

from app import dbNav
from pages.ingredient.table import ingredient_table

bp = Blueprint('ingredient', __name__) 

@bp.route("/ingredients", methods=['GET', 'POST'])
def ingredients():
    return render_template("index.html", 
                           body = ingredient_table(), 
                           activeNav = "ingredients",
                           dbNav = dbNav)