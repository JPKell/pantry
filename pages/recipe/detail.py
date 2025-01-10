from modules.recipe import Recipe

from app import db, chef

def recipe_detail(name:str) -> str:

    recipe = Recipe(name)
    totalCost = chef.totalRecipePrice(recipe)

    body = f'''
    <div class="row bg-light">
        <div class="col-xl-6 row">
            <div class="col-sm-8">
                <h1 class="text-secondary">{recipe.name.capitalize()}</h1>
            </div>
            <div class="col-sm-4 p-0 text-end">
                <table class="table table-sm table-borderless table-hover table-light mb-0">
                    <tr><td width="40%">Yield:</td><td>{recipe.yields} {recipe.yieldUnit}</td></tr>
                    <tr><td>Servings:</td><td>{recipe.servings :.1f} {recipe.servingUnit}</td></tr>
                </table>
            </div>
        </div>
        <div class="col-xl-6 row">
            <div class="col-sm-4 p-0 text-end">
                <table class="table table-sm table-borderless table-hover table-light mb-0">
                    <tr><td width="40%">Total cost:</td><td>${totalCost:.2f}</td></tr>
                    <tr><td>Servings:</td><td>${round(totalCost/recipe.servings,2):.2f}</td></tr>
                </table>
            </div>
            <div class="col-sm-4 p-0 text-end">
            </div>
            <div class="col-sm-4 p-0 text-end">
                <table class="table table-sm table-borderless table-hover table-light mb-0">
                    <tr><td width="40%">Prep:</td><td>15 minutes</td></tr>
                    <tr><td>Wait:</td><td>90-180 minutes</td></tr>
                    <tr><td>Cook:</td><td>30-45 minutes</td></tr>
                </table>
            </div>
        </div>
    </div>

    <hr class="mt-0 pt-0"/>
    
    <div class="row">
        <div class="col-lg-4 text-center h-100"> '''
    if recipe.prepareAhead:
        body += f"<h4>Prepare Ahead</h4><p>{recipe.prepareAhead.capitalize()}</p>"

    if recipe.preheat:
        body += f"<h4>Preheat</h4><p>{recipe.preheat.capitalize()} {recipe.preheatTemp} {recipe.preheatUnit}</p>"


    body += f'''
            <h4>Ingredients</h4>
            <table class="table table-sm table-borderless table-hover">
        ''' 
    for i in recipe.ingredients:
        if isinstance(i, Recipe):
            body += f'<tr><td>{i.yields} {i.yieldUnit} {i.name}</td></tr>'
        else:
            # body += f'<p class="py-0 my-0">{i.qty:.1f} {i.measurement} {i.name} {i.prep}</p>'
            body += f'<tr><td>{i.qty:.1f} {i.measurement} {i.name} {i.prep}</td></tr>'

    body += '</table>'
        # body += f'<p class="py-0 my-0">{i.qty} {i.measurement} {i.name} {i.prep}</p>'

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


    # <div class="row">
    #     <div class="col-lg-4 bg-warning">   
    #         <h2>Ingredients</h2>
    #         <ul>
    #     </div>
    #     <div class="col-lg-8 bg-info">
    #         <h2>Instructions</h2>
    #     </div>
    # </div>