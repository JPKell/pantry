from modules.database import Db

def buildNav(db:Db):
    ## Build the recipe navigation
    recipeLinks = ""
    res = db.query("SELECT category FROM recipes GROUP BY category")
    for category in res:
        recipeLinks += f'<li><a class="dropdown-item" href="/recipes/category/{category['category']}">{category['category'].capitalize()}</a><ul class="dropdown-menu dropdown-submenu">'

        subCategories = db.query(f"SELECT subcategory FROM recipes WHERE category = '{category['category']}' GROUP BY subcategory")
        for subCategory in subCategories:
            recipeLinks += f'<li><a class="dropdown-item" href="/recipes/category/{category['category']}/{subCategory['subcategory']}">{subCategory['subcategory'].capitalize()}</a><ul class="dropdown-menu dropdown-submenu">'

            recipies = db.query(f"SELECT name FROM recipes WHERE category = '{category['category']}' AND subcategory = '{subCategory['subcategory'].replace("'", "''")}'")
            for recipe in recipies:
                recipeLinks += f'<li><a class="dropdown-item" href="/recipes/{recipe['name']}">{recipe['name'].capitalize()}</a></li>'

            recipeLinks += "</ul></li>"

        recipeLinks += "</ul></li>"

    ## Build the ingredient navigation
    ingredientLinks = ""
    res = db.query("SELECT category FROM ingredients GROUP BY category")
    for category in res:
        ingredientLinks += f'<li><a class="dropdown-item" href="/ingredients/category/{category['category']}">{category['category'].capitalize()}</a><ul class="dropdown-menu dropdown-submenu">'

        subCategories = db.query(f"SELECT subcategory FROM ingredients WHERE category = '{category['category']}' GROUP BY subcategory")
        for subCategory in subCategories:
            ingredientLinks += f'<li><a class="dropdown-item" href="/ingredients/category/{subCategory['subcategory']}">{subCategory['subcategory'].capitalize()}</a><ul class="dropdown-menu dropdown-submenu">'

            recipies = db.query(f"SELECT name FROM ingredients WHERE category = '{category['category']}' AND subcategory = '{subCategory['subcategory'].replace("'", "''")}'")
            for recipe in recipies:
                ingredientLinks += f'<li><a class="dropdown-item" href="/ingredients/{recipe['name']}">{recipe['name'].capitalize()}</a></li>'

            ingredientLinks += "</ul></li>"

        ingredientLinks += "</ul></li>"

    ## Build the market navigation
    marketLinks = ""
    res = db.query("SELECT name FROM markets")
    for market in res:
        marketLinks += f'<li><a class="dropdown-item" href="/markets/{market['name']}">{market['name'].capitalize()}</a></li>'

    

    ## Database navigation
    databaseTableLinks = ""
    for table in db.get_table_names():
        databaseTableLinks += f'<a class="dropdown-item" href="/database/{table}">{table}</a></li>'


    return f"""
        <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="/">GastroTrack</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarCollapse">
            <ul class="navbar-nav me-auto mb-2 mb-md-0">
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Recipes
                    </a>
                    <ul class="dropdown-menu">
                        { recipeLinks}
                        <li><hr class="dropdown-divider"></li>
                        <li><a class="dropdown-item" href="/recipe/add">Add recipe</a></li>
                    </ul>
                </li>  
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Ingredients
                    </a>
                    <ul class="dropdown-menu">
                        { ingredientLinks }
                        <li><hr class="dropdown-divider"></li>
                        <li><a class="dropdown-item" href="/ingredients/add">Add ingredient</a></li>
                    </ul>
                </li>  
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Pantry
                    </a>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="/pantry">List</a></li>
                        <li><a class="dropdown-item" href="/pantry/add">Add ingredient</a></li>
                    </ul>
                </li>  
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Markets
                    </a>
                    <ul class="dropdown-menu">
                        { marketLinks }
                        <li><hr class="dropdown-divider"></li>
                        <li><a class="dropdown-item" href="/markets/compare">Compare</a></li>
                        <li><a class="dropdown-item" href="/markets/add">Add market</a></li>
                    </ul>
                </li>          
                <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle  {{ 'active' if activeNav == 'markets' else ''}} " href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                    Database
                </a>
                <ul class="dropdown-menu">
                    { databaseTableLinks }
                    <li><hr class="dropdown-divider"></li>
                    <li><a class="dropdown-item" href="/database/admin">Admin</a></li>
                </ul>
                </li>
            </ul>
            <form class="d-flex" role="search">
                <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                <button class="btn btn-outline-success" type="submit">Search</button>
            </form>
            </div>
        </div>
        </nav>"""