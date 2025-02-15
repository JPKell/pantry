from modules.ingredients import Ingredient
from modules.formatting import number, currency

from app import db, chef

def category_table(category:str) -> str: 
    body = f'''
    <h1>{category.capitalize()}</h1>
    <table class="table table-striped table-hover table-sm">
        <thead>
            <tr>
                <th scope="col">Name</th>
                <th scope="col">Price</th>
                <th scope="col">Size</th>
                <th scope="col">Unit</th>
            </tr>
        </thead>
        <tbody>
    '''
    ingredient = db.query(f"SELECT * FROM ingredients WHERE category = '{category}'")
    for ing in ingredient:
        ingredient = Ingredient(ing['name'])
        bestPrice =  chef.findBestIngredientPrice(ingredient)
        # print(bestPrice)
        # if bestPrice == None:
        #     bestPrice = 0
        body += f'''
        <tr>
            <td><a href="/ingredients/{ingredient.name.replace(" ", '%20')}"> {ingredient.name.capitalize()}</a></td>
            <td>${bestPrice['price']:.2f}</td>
            <td>{bestPrice['size']}</td>
            <td>{bestPrice['priceUnit']}</td>
        </tr>
        '''
    body += "</tbody></table>"
    return body