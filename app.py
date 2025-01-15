import json
from flask import Flask, render_template, request, session
from modules.database import Db
from modules.recipe import Recipe
from modules.ingredients import Ingredient
from modules.pantry import Pantry
from modules.market import Market
from modules.chef import Chef
from templates.navbar import buildNav

app     = Flask(__name__)
app.secret_key = 'gastr0tr@ck'
db      = Db(db_path="gastroTrack.db")
pantry  = Pantry()
chef    = Chef(pantry)
nav     = buildNav(db)

from pages import ingredientBlueprint, recipeBlueprint, marketBlueprint, pantryBlueprint, databaseBlueprint
app.register_blueprint(ingredientBlueprint)
app.register_blueprint(recipeBlueprint)
app.register_blueprint(marketBlueprint)
app.register_blueprint(pantryBlueprint)
app.register_blueprint(databaseBlueprint)


@app.route("/")
def web_app():
    body = "<h1>Welcome to GastroTrack</h1>"
    return render_template('index.html', body=body, nav=nav) 


## API routes
@app.route("/api/updateDb", methods=['POST'])
def addTableColumn():
    data = request.get_json()
    print("!!!",data)
    # try:
    whereClause = "AND ".join([f"{k} = '{v}'" for k,v in data['primaryKeys'].items()])
    where = f"WHERE {whereClause}" if len(whereClause) > 0 else ""
    sql = f''' UPDATE {data['table']} SET {data['column']} = "{data['value']}" { where }'''
    print(sql)
    db.execute(sql)
    return "OK", 200
    # except Exception as e:
    #     return str(e), 400