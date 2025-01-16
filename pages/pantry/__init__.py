from flask import Blueprint, json, redirect, request, session, url_for, render_template

from modules.ingredients import Ingredient

from app import db, chef, pantry, nav

bp = Blueprint('pantry', __name__) 

@bp.route("/pantry", methods=['GET', 'POST'])
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
    total = sum([x['marketDict']['total'] for x in pv.values()])
    totalSum = 0
    for i, data in pv.items():
        ingredient = Ingredient(i)
        totalSum += data['marketDict']['total']
        body += f'''
        <tr>
            <td>{ingredient.name}</td>
            <td>{data['qty']} {ingredient.unit}</td>
            <td>${data['marketDict']['total']:.2f}</td>
        </tr>'''
    body += "</tbody></table><h4>Total: ${:.2f}</h4>".format(totalSum)

    return render_template("index.html", body = body, nav = nav)