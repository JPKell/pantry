from flask import Blueprint, json, redirect, request, session, url_for, render_template

from app import dbNav, db, chef
from modules.ingredients import Ingredient
from pages.ingredient.table import ingredient_table

bp = Blueprint('database', __name__) 

@bp.route("/database/<string:table>", methods=['GET', 'POST'])
def ingredients(table:str):
    if table == "admin":
        return render_template("index.html", 
                           body =  "<h1>Admin</h1>" ,
                           activeNav = "database", dbNav = dbNav)
    

    return render_template("index.html", 
                           body =  table_table(table) ,
                           activeNav = "database", dbNav = dbNav)



def table_table(table:str):
    # Build the header for the table
    body = f''' 
    <div class="row">
        <div class="col-10">
            <h1>{table.replace("_", " ").capitalize()}</h1>
        </div>
        <div class="col-2 mt-2">
            <div class="form-check form-switch">
                <input class="form-check-input px-4 py-2 me-2 editToggle" type="checkbox" onchange="toggleEditMode(document.querySelector('.editToggle:checked'));">
                <label class="form-check-label" for="flexSwitchCheckDefault">Edit mode</label>
            </div>
        </div>
    </div>'''

    # Now start the table. Beginning with the header
    body += f'''<table id="{table}" class="table table-striped table-hover table-sm"><thead><tr>'''
    # Get the column names from the table so the list is the same as the table
    colNames = db.get_table_fields(table)
    for column in colNames:
        if column['pk'] == 1:
            print(column['name'])
        body += f'<th id="{column['name']}" {'class="primaryKey"' if column['pk'] >= 1 else ''}" scope="col">{column['name']}</th>'
    body += '</tr></thead><tbody>'

    # Now get the data from the table
    query = db.query(f"SELECT * FROM { table }")
    for r in query:
        body += '<tr class="overflow-hidden">'
        for column in colNames:
            body += f'<td {"width=15%" if column['pk'] == 1 else ''} {'class="primaryKey"' if column['pk'] == 1 else ''}>{r[column['name']]}</td>'
        body += '</tr>'

    body += "</tbody></table>"

    return body