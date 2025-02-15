from modules.ingredients import Ingredient
from modules.market import Market
from modules.formatting import number, currency

from app import db, chef

def ingredient_detail(name:str) -> str:

    ingredient = Ingredient(name)

    notes = ''
    if ingredient.notes != None:
        notes = f'''
            <div class="row bg-light">
                <div class="col text-center">
                        <b>Notes:</b> {ingredient.notes.capitalize()}
                </div>
            </div>'''

    ## pricing

    pricing_table = "<div class='col-12'><table class='table table-sm table-borderless table-striped table-hover mb-0'>"
    markets = db.query(f"SELECT * FROM markets JOIN market_ingredients ON markets.name = market_ingredients.market WHERE ingredient = '{ingredient.name.replace("'", "''")}'")
    
    prices = []
    for market in markets:
        factor =  ingredient.convert(qty=market['size'] ,fromUnit=market['priceUnit'])
        base_price = currency(market['price'] / factor, 4)
        prices.append(market['price'] / factor)
        pricing_table += f"<tr><td>{market['name'].capitalize()}</td><td>{market['brand']}</td><td>{currency(market['price'])}/{number(market['size'])} {market['priceUnit']}</td><td>{ base_price }/{ ingredient.unit } </td></tr>"

    pricing_table += "</table></div>"

    if len(prices) == 0:
        pricing_table = "<div class='col-12'><h5>No pricing data available</h5></div>"
        lowest_price = 0
        average_price = 0
        highest_price = 0
    else:       
        lowest_price = min(prices)
        average_price = sum(prices) / len(prices)
        highest_price = max(prices)

    ## conversions
    convs = db.query(f"SELECT * FROM conversions WHERE name = '{ingredient.name}'")
    conversions = f''' 
        <h3>Conversion</h3>
        <div class="row">
            <div class="col">
                <input type="text" class="form-control" placeholder="Enter quantity" aria-label="Enter quantity" aria-describedby="button-addon2">
            </div>
            <div class="col">
                <input type="text" class="form-control" placeholder="From unit" aria-label="Enter unit" aria-describedby="button-addon2">
            </div>
            <div class="col">
                <input type="text" class="form-control" placeholder="To unit" aria-label="Enter unit" aria-describedby="button-addon2">
            </div>
        </div>
        <table class="table table-sm table-borderless table-hover mb-0">
        <thead><tr><th>Unit</th><th>Factor</th></tr></thead>
    '''
    for c in convs:
        conversions += f"<tr><td>{c['fromMeasure']}</td><td>{c['factor']}</td></tr>"
    conversions += f"""</table>"""

    ## Recipies its used in
    recipeHtml = ''
    recipes = db.query(f"SELECT r.name FROM recipe_ingredients ri JOIN recipes r ON r.id = ri.recipe_id WHERE ri.ingredient = '{ingredient.name.replace("'", "''")}' GROUP BY r.name")
    if len(recipes) > 0:

        recipeHtml = '<div class="col-lg-4 col-sm-6"><h4>Used in</h4><table class="table table-sm table-borderless table-striped table-hover mb-0">'
        for recipe in recipes:
            recipeHtml += f'<tr><td><a href="/recipes/{recipe['name']}">{recipe['name'].capitalize()}</a></td></tr>'
        recipeHtml += "</table></div>"

    ## Alternatives
    altHtml = ''
    if len(ingredient.alternatives) > 0:
        altHtml = '<div class="col-lg-4 col-sm-6"><h4>Alternatives</h4><table class="table table-sm table-borderless table-striped table-hover mb-0">'
        for alt in ingredient.alternatives:
            altHtml += f'<tr><td><a href="/ingredients/{alt}">{alt.capitalize()}</a></td></tr>'
        altHtml += "</table></div>"


    body = f'''
    <div class="row bg-light">
        <div class="col-xl-6 row">
            <div class="col-sm-8 d-flex align-items-center justify-content-center">
                <h1 class="text-secondary text-center ">{ingredient.displayName.capitalize()}</h1>
            </div>
            <div class="col-sm-4 p-0 d-flex align-items-center justify-content-center">
                <table class="table table-sm table-borderless table-hover table-light mb-0">
                    <tr><td><b>{ingredient.category.capitalize()}, {ingredient.subcategory.capitalize()}</b></td></tr>
                    <tr><td>Shelf life {ingredient.shelfLife} days</td></tr>
                </table>    
            </div>
        </div>
        <div class="col-xl-6 row">
            <div class="col-sm-4 p-0 d-flex align-items-center justify-content-center">
                <table class="table table-sm table-borderless table-hover table-light mb-0">
                    <tr><td>Kosher: {ingredient.kosher.capitalize()}</td></tr>
                    <tr><td>Default unit: {ingredient.unit}</td></tr>
                </table>    
            </div>
            <div class="col-sm-8 p-0 d-flex align-items-center justify-content-center">
                <table class="table table-sm table-borderless table-hover table-light mb-0">
                    <tr><td>Raw storage: {ingredient.rawStorage.capitalize()}</td></tr>
                    <tr><td>Processed storage: {ingredient.processedStorage.capitalize()}</td></tr>
                </table>   
            </div>
        </div>
    </div>
    {notes}
    <hr class="mt-0 pt-0"/>

    <div class="row">
        <div class="col-xl-6 row">
            <div class="col-sm-8 d-flex align-items-center justify-content-center">
                <h4 class="text-secondary text-center ">Market pricing</h1>
            </div>
            <div class="col-sm-4 p-0 d-flex align-items-center justify-content-center">
                <table class="table table-sm table-borderless table-hover mb-0">
                    <tr><td>Lowest price: {currency(lowest_price,4)}/{ingredient.unit}</td></tr>
                </table>    
            </div>
        </div>
        <div class="col-xl-6 row">
            <div class="col-sm-4 p-0 d-flex align-items-center justify-content-center">
                <table class="table table-sm table-borderless table-hover mb-0">
                    <tr><td>Avg Price: {currency(average_price,4)}/{ingredient.unit}</td></tr>
                </table>    
            </div>
            <div class="col-sm-8 p-0 d-flex align-items-center justify-content-center">
                <table class="table table-sm table-borderless table-hover mb-0">
                    <tr><td>Highest price: {currency(highest_price,4)}/{ingredient.unit}</td></tr>
                </table>   
            </div>
        </div>


        <div class="row pt-3 pb-3">
            <div class="col-sm-3 p-2 d-flex align-items-center justify-content-center">
                <h5 class="text-secondary text-center ">Compare</h5>
            </div>
            <div class="col-sm-3 p-2 d-flex align-items-center justify-content-center">
                <input type="number" class="form-control" placeholder="Price" aria-label="Enter price" aria-describedby="button-addon2">  
            </div>

            <div class="col-sm-3 p-2 d-flex align-items-center justify-content-center">
                <input type="number" class="form-control" placeholder="Size" aria-label="Enter price" aria-describedby="button-addon2"> 
            </div>
            <div class="col-sm-3 p-2 d-flex align-items-center justify-content-center">
                <input type="text" class="form-control" placeholder="Units" aria-label="Enter price" aria-describedby="button-addon2">   
            </div>
        </div>
        {pricing_table}
    </div>
    <hr class="mt-0 pt-0"/>
    <div class="row justify-content-center">
        <div class="col-lg-4">
            { conversions }
        </div>
        { recipeHtml }
        { altHtml }
    </div>
        '''

    return body

