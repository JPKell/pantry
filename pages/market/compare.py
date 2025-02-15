from modules.ingredients import Ingredient
from modules.market import Market
from modules.formatting import number, currency

from app import db, chef

def market_compare() -> str:

    # market = Market(name)

    # Get list of all ingredients
    ingredients = db.query("SELECT * FROM ingredients ORDER BY name")
    markets = db.query("SELECT * FROM markets WHERE name != 'home' ORDER BY name")

    body = f'''
    <div class="row bg-light">
        <div class="col-xl-6 row">
            <div class="col-sm-8 d-flex align-items-center justify-content-center">
                <h1 class="text-secondary text-center ">Comparisons</h1>
            </div>
            <div class="col-sm-4 p-0 d-flex align-items-center justify-content-center">
                  
            </div>
        </div>
        <div class="col-xl-6 row ">

        </div>
    </div>
    <hr class="mt-0 pt-0"/>
    <div class="row">
        <table id="market_ingredients" class="table table-striped table-hover table-sm">
            <thead >
                <tr class="overflow-hidden">
                    <th id="market" scope="col">Ingredient</th>'''
    
    for market in markets:
        body += f'<th scope="col">{market['name'].capitalize()}</th>'

    body += '''</tr></thead><tbody>'''
    # Create the table for the ingredients
    for ingredient in ingredients:
        ingredient = Ingredient(ingredient['name'])
        # Get the price of the ingredient at the market
        details = db.query(f"SELECT * FROM market_ingredients WHERE ingredient = '{ingredient.name}' order by ingredient")
        details = {d['market']: d for d in details}

        body += f'''<tr class="overflow-hidden">
            <td class="primaryKey"><a href="/ingredients/{ingredient.name.replace(" ", "%20")}">{ingredient.name.capitalize()}</a></td>'''
        for market in markets:
            if market['name'] in details:
                detail = details[market['name']]
                price = detail['price'] / ingredient.convert(detail['size'], fromUnit=detail['priceUnit'])
                price = currency(price, 3)
                body += f'<td>{price} /{ingredient.unit}</td>'
            else:
                body += f'<td></td>'

        body += '</tr>'
        
    
    body += f'</tbody></table></div>'

    return body

