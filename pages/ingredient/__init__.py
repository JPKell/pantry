from flask import Blueprint, json, redirect, request, session, url_for, render_template

from app import nav
from pages.ingredient.table import ingredient_table
from pages.ingredient.detail import ingredient_detail


bp = Blueprint('ingredient', __name__) 

@bp.route("/ingredients/<string:name>")
@bp.route("/ingredients")
def ingredients(name:str=None):
    if name != None:
        # try:
            return render_template("index.html", 
                                   body = ingredient_detail(name), 
                                   nav = nav)
        # except Exception as e:
        #     html = f"""<div class="text-center p-5 m-5"><h1>Error when loading {name}</h1><p>{e}</p></div>"""
        #     return render_template("index.html", 
        #                            body = html, 
        #                            nav = nav)
    return render_template("index.html", 
                           body = ingredient_table(), 
                           nav = nav)