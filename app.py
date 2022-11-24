import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from flask_paginate import Pagination, get_page_args
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# Pagination item limit per page
PER_PAGE = 3


# Pagination
# used code from
# https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9
def paginated(recipes):
    """ Sets Pagination for long content pages """
    page, per_page, offset = get_page_args(
                            page_parameter='page',
                            per_page_parameter='per_page')
    offset = page * PER_PAGE - PER_PAGE

    return recipes[offset: offset + PER_PAGE]


def pagination_args(recipes):
    page, per_page, offset = get_page_args(
                            page_parameter='page',
                            per_page_parameter='per_page')
    total = len(recipes)

    return Pagination(page=page, per_page=PER_PAGE, total=total)


@app.errorhandler(404)
def not_found(e):
    # To return error page when a 404 error occurs
    return render_template("404.html")


@app.route("/")
# link to homepage
@app.route("/go_home")
def go_home():
    return render_template("home.html")


# Recipe page showing all recipes
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    ingredients1 = list(mongo.db.recipes.ingredients1.find())
    recipes_paginated = paginated(recipes)
    pagination = pagination_args(recipes)
    return render_template("recipes.html",
                           recipes=recipes_paginated,
                           ingredients1=ingredients1,
                           pagination=pagination)


# Search box on recipe pages
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    recipes_paginated = paginated(recipes)
    pagination = pagination_args(recipes)
    categories = mongo.db.categories.find().sort("category_name", -1)
    return render_template("recipes.html", recipes=recipes_paginated,
                           pagination=pagination,
                           categories=categories)


# filter function to show each course
@app.route("/recipes_by_category/<category_name>")
def get_recipes_by_category(category_name):
    recipes = list(mongo.db.recipes.find({"category_name": category_name}))
    recipes_paginated = paginated(recipes)
    pagination = pagination_args(recipes)
    return render_template("recipes_filter.html", recipes=recipes_paginated,
                           pagination=pagination, category_name=category_name)


# filter function for difficulty level
@app.route("/recipes_by_difficulty/<difficulty>")
def get_recipes_by_difficulty(difficulty):
    recipes = list(mongo.db.recipes.find({"difficulty": difficulty}))
    recipes_paginated = paginated(recipes)
    pagination = pagination_args(recipes)
    return render_template("recipes_filter.html", recipes=recipes_paginated,
                           pagination=pagination, difficulty=difficulty)


# register functionality
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # check if username already exists
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "favourite": request.form.get("favourite").lower(),
            "chef_level": request.form.get("chef_level").lower()
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("You are now registered!")
        return redirect(
            url_for("profile", username=session["user"]))
    return render_template("register.html")


# login function
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # password check
        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Hey there {}!".format(request.form.get("username")))
                    return redirect(
                        url_for("profile", username=session["user"]))
            else:
                flash("Incorrect username or password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect username or password")
            return redirect(url_for("login"))
    return render_template("login.html")


# profile page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username
    username = mongo.db.users.find_one(
        {"username": username})
    recipes = list(mongo.db.recipes.find())
    return render_template("profile.html", recipes=recipes, username=username)

    if session["user"]:
        return render_template("profile.html", user=username)
    # redirect to login page if not logged in
    return redirect(url_for("login"))


# logout function
@app.route("/logout")
def logout():
    flash("You have now logged out")
    session.pop("user")
    return redirect(url_for("login"))


# add recipe function
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    # retrieve data from form
    if request.method == "POST":
        new_recipe = {
            "category_name": request.form.get("category_name"),
            "food_name": request.form.get("food_name"),
            "food_img": request.form.get("food_img"),
            "description": request.form.get("description"),
            "time": request.form.get("time"),
            "difficulty": request.form.get("difficulty"),
            "ingredients1": request.form.getlist("ingredients1"),
            "method1": request.form.getlist("method1"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(new_recipe)
        flash("Your recipe is now added!")
        return redirect(url_for("get_recipes"))
    categories = mongo.db.categories.find().sort("category_name", -1)
    return render_template("add_recipe.html", categories=categories)


# edit recipe function
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        submit_recipe = {
            "category_name": request.form.get("category_name"),
            "food_name": request.form.get("food_name"),
            "food_img": request.form.get("food_img"),
            "description": request.form.get("description"),
            "time": request.form.get("time"),
            "difficulty": request.form.get("difficulty"),
            "ingredients1": request.form.getlist("ingredients1"),
            "method1": request.form.getlist("method1"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit_recipe)
        flash("Your recipe has been updated!")
        return redirect(url_for("get_single_recipe",
                                recipe_id=recipe_id))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", -1)
    return render_template("edit_recipe.html",
                           recipe=recipe, categories=categories)


# delete recipe function
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Your recipe has now been deleted")
    return redirect(url_for("get_recipes"))


# Admin functions

# retrieve list of recipe names
@app.route("/get_names")
def get_names():
    recipes = list(mongo.db.recipes.find())
    return render_template("manage.html", recipes=recipes)


# function to delete any recipe
@app.route("/admin_delete_recipe/<recipe_id>")
def admin_delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Your recipe has now been deleted")
    return redirect(url_for("get_names"))


# function for admin/user to click recipe name to show full details
@app.route("/get_single_recipe/<recipe_id>")
def get_single_recipe(recipe_id):
    recipes = list(mongo.db.recipes.find({"_id": ObjectId(recipe_id)}))
    return render_template("one_recipe.html", recipes=recipes)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
