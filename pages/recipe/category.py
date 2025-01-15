from modules.recipe import Recipe
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
                <th scope="col">Yields</th>
                <th scope="col">YieldUnit</th>
                <th scope="col">Servings</th>
                <th scope="col">ServingUnit</th>
                <th scope="col">Price per Serving</th>
            </tr>
        </thead>
        <tbody>
    '''
    recipes = db.query(f"SELECT * FROM recipes WHERE category = '{category}'")
    for r in recipes:
        recipe = Recipe(r['name'])
        body += f'''
        <tr>
            <td><a href="/recipes/{recipe.name.replace(" ", '%20')}"> {recipe.name.capitalize()}</a></td>
            <td>${chef.totalRecipePrice(recipe):.2f}</td>
            <td>{number(recipe.yields)}</td>
            <td>{recipe.yieldUnit}</td>
            <td>{number(recipe.servings)}</td>
            <td>{recipe.servingUnit}</td>
            <td>{currency(chef.totalRecipePrice(recipe) / recipe.servings)}</td>
        </tr>
        '''
    body += "</tbody></table>"
    return body