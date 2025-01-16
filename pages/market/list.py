from modules.ingredients import Ingredient
from modules.market import Market
from modules.formatting import number, currency

from app import db, chef

def market_list(name:str) -> str:

    market = Market(name)

    # Get list of all ingredients
    ingredients = db.query("SELECT * FROM ingredients ORDER BY name")


    body = f'''
    <div class="row bg-light">
        <div class="col-xl-6 row">
            <div class="col-sm-8 d-flex align-items-center justify-content-center">
                <h1 class="text-secondary text-center ">{market.name.capitalize()}</h1>
            </div>
            <div class="col-sm-4 p-0 d-flex align-items-center justify-content-center">
                <table class="table table-sm table-borderless table-hover table-light mb-0">
                    <tr><td><b><a target="_blank" href="https://www.google.ca/maps/place/{market.location.replace(" ",'+')}">{market.location}</a></b></td></tr>
                    <tr><td>{market.distance} km</td></tr>
                </table>    
            </div>
        </div>
        <div class="col-xl-6 row ">
            <div class="col-10"></div>
            <div class="col-2 form-check form-switch d-flex align-items-center justify-content-center">
                <input id="editCheck" class="form-check-input px-4 py-2 me-2 editToggle" type="checkbox" onchange="toggleEditMode(document.querySelector('.editToggle:checked'));">
                <label for="editCheck">Edit</label>
            </div>
        </div>
    </div>
    <hr class="mt-0 pt-0"/>
    <div class="row">
        <table id="market_ingredients" class="table table-striped table-hover table-sm">
            <thead >
                <tr class="overflow-hidden">
                    <th id="market" width="5%" class="primaryKey" scope="col">Name</th>
                    <th id="ingredient" class="primaryKey" scope="col">Ingredient</th>
                    <th id="price" class="typeNumber" scope="col">Price</th>
                    <th id="priceUnit" scope="col">Unit</th>
                    <th id="size" class="typeNumber" scope="col">Size</th>
                    <th id="brand" scope="col">Brand</th>
                </tr>
            </thead>
            <tbody>
    '''
    # Create the table for the ingredients
    for ingredient in ingredients:
        ingredient = Ingredient(ingredient['name'])
        # Get the price of the ingredient at the market
        details = db.queryOne(f"SELECT * FROM market_ingredients WHERE market = '{market.name}' AND ingredient = '{ingredient.name}' order by ingredient")

        price = None
        unit = None
        size = None
        brand = None
        if details:
            price = details['price']
            unit = details['priceUnit']
            size = details['size']
            brand = details['brand']

        body += f'''
            <tr class="overflow-hidden">
                <td class="primaryKey">{market.name}</td>
                <td class="primaryKey"><a href="{market.search}{ingredient.name.replace(" ", "%20")}" target="_blank">{ingredient.name.capitalize()}</a></td>
                <td>{currency(price) if price else ''}</td>
                <td>{ingredient.unit if unit else ''}</td>
                <td>{number(size) if size else ''}</td>
                <td>{brand if brand else ''}</td>
            </tr>
        '''
    
    body += f'</tbody></table></div>'

    return body

