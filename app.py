import json
from flask import Flask, render_template, request, session
from modules.database import Db
from modules.recipe import Recipe
from modules.ingredients import Ingredient
from modules.pantry import Pantry
from modules.market import Market
from modules.chef import Chef

app = Flask(__name__)
app.secret_key = 'the random string'
db = Db(db_path="gastroTrack.db")
pantry = Pantry()
chef = Chef(pantry)


@app.route("/")
def web_app():
    body = "<h1>Welcome to GastroTrack</h1>"
    return render_template('index.html', body=body) 

@app.route("/ingredients")
def settings_page():
    body = f'''
    <h1>Ingredients</h1>
    <table class="table table-striped table-hover table-sm">
        <thead>
            <tr>
                <th scope="col">Name</th>
                <th scope="col">Unit</th>
                <th scope="col">Best Price</th>
                <th scope="col">Location</th>
                <th scope="col">Size</th>
            </tr>
        </thead>
        <tbody>
    '''
    ingredients = db.query("SELECT * FROM ingredients")
    for i in ingredients:
        ingredient = Ingredient(i['name'], qty=1)
        bestPrice = chef.findBestIngredientPrice(ingredient)
        body += f'''
        <tr>
            <td>{ingredient.name}</td>
            <td>{ingredient.measurement}</td>
            <td>${bestPrice['price']}</td>
            <td>{bestPrice['market']}</td>
            <td>{bestPrice['size']} {bestPrice['priceUnit']}</td>
        </tr>
        '''
    body += "</tbody></table>"

    return render_template("index.html", body = body)

@app.route("/recipes")
def recipes_page():
    body = f'''
    <h1>Recipes</h1>
    <table class="table table-striped table-hover table-sm">
        <thead>
            <tr>
                <th scope="col">Name</th>
                <th scope="col">Price</th>
                <th scope="col">Yields</th>
                <th scope="col">YieldUnit</th>
                <th scope="col">Servings</th>
                <th scope="col">ServingUnit</th>
                <th scope="col">Price per Serving</th>
            </tr>
        </thead>
        <tbody>
    '''
    recipes = db.query("SELECT * FROM recipes")
    for r in recipes:
        recipe = Recipe(r['name'])
        body += f'''
        <tr>
            <td>{recipe.name}</td>
            <td>${chef.totalRecipePrice(recipe):.2f}</td>
            <td>{recipe.yields}</td>
            <td>{recipe.yieldUnit}</td>
            <td>{round(recipe.servings, 1)}</td>
            <td>{recipe.servingUnit}</td>
            <td>${round(chef.totalRecipePrice(recipe) / recipe.servings, 3)}</td>
        </tr>
        '''
    body += "</tbody></table>"

    return render_template("index.html", body = body)

@app.route("/pantry")
def pantry_page():
    body = f'''
    <h1>Pantry</h1>
    <table class="table table-striped table-hover table-sm">
        <thead>
            <tr>
                <th scope="col">Name</th>
                <th scope="col">Quantity</th>
                <th scope="col">Cost</th>
            </tr>
        </thead>
        <tbody>
    '''
    pv = chef.detailedPantryValue()

    for i, data in pv.items():
        ingredient = Ingredient(i)
        body += f'''
        <tr>
            <td>{ingredient.name}</td>
            <td>{data['qty']} {ingredient.measurement}</td>
            <td>${data['marketDict']['total']:.2f}</td>
        </tr>'''
    body += "</tbody></table>"

    return render_template("index.html", body = body)

@app.route("/markets")
def market_page():
    return render_template("index.html")


## API routes
@app.route("/api/addTableColumn/<string:tableName>", methods=['POST'])
def addTableColumn(tableName:str):
    ...