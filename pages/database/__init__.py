from flask import Blueprint, json, redirect, request, session, url_for, render_template

from app import nav, db, chef
from modules.ingredients import Ingredient
from modules.formatting import number
from pages.ingredient.table import ingredient_table

bp = Blueprint('database', __name__) 

@bp.route("/database/<string:table>", methods=['GET', 'POST'])
def ingredients(table:str):
    if table == "admin":
        return render_template("index.html", 
                           body =  "<h1>Admin</h1>" ,
                           nav = nav)
    

    return render_template("index.html", 
                           body =  table_table(table) ,
                           nav = nav)



def table_table(table:str):
    # Build the header for the table
    body = f''' 
    <div class="row">
        <div class="col-sm-10">
            <h1>{table.replace("_", " ").capitalize()}</h1>
        </div>
        <div class="col-sm d-flex align-items-center justify-content-center">
            <div class="form-check form-switch">
                <input id="editCheck" class="form-check-input px-4 py-2 me-2 editToggle" type="checkbox" onchange="toggleEditMode(document.querySelector('.editToggle:checked'));">
                <label for="editCheck">Edit</label>
            </div>
        </div>
    </div>'''

    # Now start the table. Beginning with the header
    body += f'''<table id="{table}" class="table table-striped table-hover table-sm"><thead><tr>'''
    # Get the column names from the table so the list is the same as the table
    colNames = db.get_table_fields(table)
    for column in colNames:
        # if column['pk'] == 1:
        body += f'<th id="{column['name']}" {'class="primaryKey pe-5"' if column['pk'] >= 1 else ''}" scope="col">{column['name']} {'(PK)' if column['pk'] >= 1 else ''}</th>'
    body += '</tr></thead><tbody>'

    # Now get the data from the table
    query = db.query(f"SELECT * FROM { table }")
    for r in query:
        body += '<tr class="overflow-hidden">'
        for column in colNames:
            isNum = True if column['type'] in ["INTEGER", "REAL"] and r[column['name']] != None else False
            body += f'<td class="{'primaryKey' if column['pk'] >= 1 else ''} ">{r[column['name']] if not isNum else number(r[column['name']], roundTo=None)}</td>'
        body += '</tr>'

    body += "</tbody></table>"

    return body