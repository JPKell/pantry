from flask import Blueprint, json, redirect, request, session, url_for, render_template

from pages.recipe.table import recipe_table
from pages.recipe.detail import recipe_detail

bp = Blueprint('recipe', __name__) 

@bp.route("/recipes/<string:name>", methods=['GET', 'POST'])
@bp.route("/recipes", methods=['GET', 'POST'])
def recipes_page(name:str=None):
    if name == None:
        return render_template("index.html", body = recipe_table(), activeNav = "recipes")
    else:
        try:
            return render_template("index.html", body = recipe_detail(name), activeNav = "recipes")
        except Exception as e:
            html = f"""<div class="text-center p-5 m-5"><h1>Error when loading {name}</h1><p>{e}</p></div>"""
            return render_template("index.html", body = html, activeNav = "recipes")