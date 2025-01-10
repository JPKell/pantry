import json
from flask import Flask, render_template, request, session
from modules.database import Db
from modules.recipe import Recipe
from modules.ingredients import Ingredient
from modules.pantry import Pantry
from modules.market import Market
from modules.chef import Chef

app     = Flask(__name__)
app.secret_key = 'gastr0tr@ck'
db      = Db(db_path="gastroTrack.db")
pantry  = Pantry()
chef    = Chef(pantry)
dbNav   = ""
for table in db.get_table_names():
    dbNav += f'</li><a class="dropdown-item" href="/database/{table}">{table}</a></li>'

from pages import ingredientBlueprint, recipeBlueprint, marketBlueprint, pantryBlueprint, databaseBlueprint
app.register_blueprint(ingredientBlueprint)
app.register_blueprint(recipeBlueprint)
app.register_blueprint(marketBlueprint)
app.register_blueprint(pantryBlueprint)
app.register_blueprint(databaseBlueprint)


@app.route("/")
def web_app():
    body = "<h1>Welcome to GastroTrack</h1>"
    return render_template('index.html', body=body) 


## API routes
@app.route("/api/editDb", methods=['POST'])
def addTableColumn():
    data = request.get_json()
    print("!!!",data)
    return "OK", 500