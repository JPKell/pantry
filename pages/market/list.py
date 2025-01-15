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
                    <tr><td><b>{market.location}</b></td></tr>
                    <tr><td>{market.distance} km</td></tr>
                </table>    
            </div>
        </div>
        <div class="col-xl-6 row">
        </div>
    </div>
    <hr class="mt-0 pt-0"/>
    <div class="row">
        <table class="table table-striped table-hover table-sm">
            <thead>
                <tr>
                    <th>Ingredient</th>
                    <th>Price</th>
                    <th>Unit</th>
                    <th>Size</th>
                    <th>Cost</th>
                    <th>Brand</th>
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
        cost = None
        brand = None
        if details:
            price = details['price']
            unit = details['priceUnit']
            size = details['size']
            cost = details['price']
            brand = details['brand']

        body += f'''
            <tr>
                <td><a href="{market.search}{ingredient.name.replace(" ", "%20")}" target="_blank">{ingredient.name.capitalize()}</a></td>
                <td>{currency(price) if price else ''}</td>
                <td>{ingredient.unit if unit else ''}</td>
                <td>{number(size) if size else ''}</td>
                <td>{currency(cost) if cost else ''}</td>
                <td>{brand if brand else ''}</td>
            </tr>
        '''


    body += f'''
    </div>
        '''

    return body

