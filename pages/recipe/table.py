from modules.recipe import Recipe

from app import db, chef

def recipe_table() -> str: 
    body = f'''
    <h1>Recipes</h1>
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
    recipes = db.query("SELECT * FROM recipes")
    for r in recipes:
        recipe = Recipe(r['name'])
        body += f'''
        <tr>
            <td>{recipe.name}</td>
            <td>${chef.totalRecipePrice(recipe):.2f}</td>
            <td>{recipe.yields}</td>
            <td>{recipe.yieldUnit}</td>
            <td>{round(recipe.servings, 1)}</td>
            <td>{recipe.servingUnit}</td>
            <td>${round(chef.totalRecipePrice(recipe) / recipe.servings, 3)}</td>
        </tr>
        '''
    body += "</tbody></table>"
    return body