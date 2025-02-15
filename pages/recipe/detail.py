from modules.recipe import Recipe
from modules.formatting import number, currency

from app import db, chef

def recipe_detail(name:str) -> str:

    recipe = Recipe(name)
    totalCost = chef.totalRecipePrice(recipe)

    body = f'''
    <div class="row bg-light">
        <div class="col-xl-6 row">
            <div class="col-sm-8 d-flex align-items-center justify-content-center">
                <h1 class="text-secondary text-center ">{recipe.name.capitalize()}</h1>
            </div>
            <div class="col-sm-4 p-0 d-flex align-items-center text-end">
                <table class="table table-sm table-borderless table-hover table-light mb-0">
                    <tr><td width="40%">Yield:</td><td>{number(recipe.yields)} {recipe.yieldUnit}</td></tr>
                    <tr><td>Servings:</td><td>{number(recipe.servings)} {recipe.servingUnit}</td></tr>
                </table>
            </div>
        </div>
        <div class="col-xl-6 row">
            <div class="col-sm-4 p-0 d-flex align-items-center text-end">
                <table class="table table-sm table-borderless table-hover table-light mb-0">
                    <tr><td width="40%">Total cost:</td><td>{currency(totalCost)}</td></tr>
                    <tr><td>Servings:</td><td>{currency(totalCost/recipe.servings)}</td></tr>
                </table>
            </div>
            <div class="col-sm-4 p-0 text-end">
            </div>
            <div class="col-sm-4 p-0 d-flex align-items-center text-end"> '''
    

    if recipe.times != {}: 
        body += f'<table class="table table-sm table-borderless table-hover table-light mb-0">'   

        for name, times in recipe.times.items():  
            body += f'<tr><td width="40%">{name.capitalize()}:</td><td>{times}</td></tr>'
        body += f'''</table> '''
    
    body += f'''</div></div></div>
        <hr class="mt-0 pt-0"/>
        <div class="row">
            <div class="col-lg-4 text-center h-100"> '''
    if recipe.prepareAhead:
        body += f"<h4>Prepare Ahead</h4><p>{recipe.prepareAhead.capitalize()}</p>"

    if recipe.preheat:
        body += f"<h4>Preheat</h4><p>{recipe.preheat.capitalize()} {number(recipe.preheatTemp, 0) if recipe.preheatTemp != None else ''} {recipe.preheatUnit if recipe.preheatUnit else ''}</p>"

    body += f'''
            <h4>Ingredients</h4>
            <table class="table table-sm table-borderless table-hover">
        ''' 

    # Split the recipe ingredients into parts if required 
    for part in list(set([x.recipePart for x in recipe.ingredients ])):
        if part != None:
            body += f'<tr><th>{part.capitalize()}</th></tr>'
        for ingred in [ ri for ri in recipe.ingredients if ri.recipePart == None or ri.recipePart == part ]:
            if isinstance(ingred, Recipe):
                body += f'<tr><td>{number(ingred.yields, 0) if ingred.yields > 5 else number(ingred.yields) } {ingred.yieldUnit} {ingred.name}</td></tr>'
            else:
                _unit = ingred.unit if ingred.unit != 'each' else ''
                s = 's' if ingred.qty > 1 and ingred.unit == 'each' else ''
                body += f'<tr><td>{number(ingred.qty,0) if ingred.qty > 5 else number(ingred.qty)} {_unit} {ingred.displayName}{s} {ingred.prep if ingred.prep else ''}</td></tr>'

    body += '</table>'

    if recipe.notes:
        body += f"<h5>Notes</h5><p>{recipe.notes.capitalize()}</p>"


    body += '''
        </div>
        <div class="col-lg-8">
            <h2>Instructions</h2>
            <table class="table table-hover">
        '''
    for s in recipe.steps:
        body += f'''<tr class"row">
                
                <td><input class="form-check-input p-3 btn-secondary" type="checkbox" value="" id="f"></td>
                <td class>{s}</td>
                </tr>'''

    body += '''
            </ul>
        </div>
    </div>
        '''

    return body

