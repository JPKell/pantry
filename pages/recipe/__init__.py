from flask import Blueprint, json, redirect, request, session, url_for, render_template

from pages.recipe.category import category_table
from pages.recipe.subcategory import subcategory_table
from pages.recipe.table import recipe_table
from pages.recipe.detail import recipe_detail
from app import nav
bp = Blueprint('recipe', __name__) 

@bp.route("/recipes/<string:name>", methods=['GET', 'POST'])
@bp.route("/recipes", methods=['GET', 'POST'])
def recipes_page(name:str=None):
    if name == None:
        return render_template("index.html", body = recipe_table(), nav = nav)
    else:
        try:
            return render_template("index.html", body = recipe_detail(name), nav = nav)
        except Exception as e:
            html = f"""<div class="text-center p-5 m-5"><h1>Error when loading {name}</h1><p>{e}</p></div>"""
            return render_template("index.html", body = html, nav = nav)
        

@bp.route("/recipes/category/<string:category>")
def recipes_category(category:str):
    try:
        return render_template("index.html", body = category_table(category), nav = nav)
    except Exception as e:
        html = f"""<div class="text-center p-5 m-5"><h1>Error when loading {category}</h1><p>{e}</p></div>"""
        return render_template("index.html", body = html, nav = nav)
    
@bp.route("/recipes/category/<string:category>/<string:subcategory>")
def recipes_subcategory(category:str, subcategory:str):
    try:
        return render_template("index.html", body = subcategory_table(category, subcategory), nav = nav)
    except Exception as e:
        html = f"""<div class="text-center p-5 m-5"><h1>Error when loading {category}</h1><p>{e}</p></div>"""
        return render_template("index.html", body = html, nav = nav)