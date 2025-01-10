from modules.ingredients import Ingredient

from app import db, chef

def ingredient_table():
    body = f'''
    <div class="row">
        <div class="col-10">
            <h1>Ingredients</h1>
        </div>
        <div class="col-2 mt-2">
            <div class="form-check form-switch">
                <input class="form-check-input px-4 py-2 me-2 editToggle" type="checkbox" onchange="toggleEditMode(document.querySelector('.editToggle:checked'));">
                <label class="form-check-label" for="flexSwitchCheckDefault">Edit mode</label>
            </div>
        </div>
    </div>
    <table id="ingredients" class="table table-striped table-hover table-sm">
        <thead>
            <tr>
                <th id="name" scope="col" width="10%">Name</th>
                <th id="displayName" scope="col">displayName</th>
                <th id="units" scope="col">Units</th>
                <th id="size" scope="col">Size</th>
                <th id="rawStorage" scope="col">Raw storage</th>
                <th id="processedStorage" scope="col">Processed storage</th>
                <th id="shelfLife" scope="col">Shelf life</th>
                <th id="notes" scope="col" width="10%">Notes</th>
                <th id="tags" scope="col" width="10%">Tags</th>
                <th id="category" scope="col">Category</th>
                <th id="subcategory" scope="col">Subcategory</th>
                <th id="kosher" scope="col">Kosher</th>
            </tr>
        </thead>
        <tbody>
    '''
    ingredients = db.query("SELECT * FROM ingredients")
    for i in ingredients:
        ingredient = Ingredient(i['name'], qty=1)
        bestPrice = chef.findBestIngredientPrice(ingredient)
        body += f'''
        <tr class="overflow-hidden">
            <td>{ingredient.name}</td>
            <td>{ingredient.displayName}</td>
            <td>{ingredient.measurement}</td>
            <td>{ingredient.size}</td>
            <td>{ingredient.rawStorage}</td>
            <td>{ingredient.processedStorage}</td>
            <td>{ingredient.shelfLife}</td>
            <td>{ingredient.notes}</td>
            <td>{ingredient.tags}</td>
            <td>{ingredient.category}</td>
            <td>{ingredient.subcategory}</td>
            <td>{ingredient.kosher}</td>
        </tr>
        '''
    body += "</tbody></table>"

    return body