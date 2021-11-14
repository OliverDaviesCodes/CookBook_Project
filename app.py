import os
import cloudinary
import cloudinary.uploader
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


UPLOAD_FOLDER = '/static/media'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

cloudinary.config(
    cloud_name=os.environ.get("CLOUD_NAME"),
    api_key=os.environ.get("API_KEY"),
    api_secret=os.environ.get("API_SECRET")
)

mongo = PyMongo(app)


def is_logged_in():
    """
    This function determines if the user is logged in
    """
    return session.get("user")


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    """
    Returns all recipes needed on recipes.html
    """
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/recipe/<recipe_id>", methods=["GET"])
def get_recipe(recipe_id):
    """
    Returns a single recipe
    """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("show_recipe.html", recipe=recipe)


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    This is the search function on the search bar
    """
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    This generates the register functionality to the database
    """
    if request.method == "POST":
        # check if username exists in the db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            # Takes you back to registration
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into "session" cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Succesful")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    This generates the login functionality to the database
    """
    if request.method == "POST":
        # check to see if username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensures hashed password matches user input
            if check_password_hash(
               existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile", methods=["GET"])
def profile():
    """
    This generates the users profile
    """
    if is_logged_in():
        # retrieves the session users username from the database
        user = mongo.db.users.find_one({"username": session["user"]})
        recipes = mongo.db.recipes.find({"created_by": session["user"]})
        return render_template("profile.html", user=user, recipes=recipes)
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """
     remove user from the session cookies
    """
    if is_logged_in():
        # remove user from the session cookies
        flash("You have been logged out")
        session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    """
    This is the recipe generation method
    """
    if request.method == "POST":
        image = request.files["image"]
        if image and image.filename.split(
                                        ".")[-1].lower() in ALLOWED_EXTENSIONS:
            upload_result = cloudinary.uploader.upload(image)

        is_vegetarian = "on" if request.form.get("is_vegetarian") else "off"
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "category_name": request.form.get("category_name"),
            "recipe_time": request.form.get("recipe_time"),
            "portions": request.form.get("portions"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_instructions": request.form.get("recipe_instructions"),
            "is_vegetarian": is_vegetarian,
            "created_by": session["user"],
            "url": upload_result["secure_url"],
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("get_recipes"))
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipes.html", categories=categories)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    """
    This is the edit recipe functionality
    """
    if request.method == "POST":
        is_vegetarian = "on" if request.form.get("is_vegetarian") else "off"
        submit = {
            "recipe_name": request.form.get("recipe_name"),
            "category_name": request.form.get("category_name"),
            "recipe_time": request.form.get("recipe_time"),
            "portions": request.form.get("portions"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_instructions": request.form.get("recipe_instructions"),
            "is_vegetarian": is_vegetarian,
            "created_by": session["user"]
        }
        mongo.db.tasks.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Updated")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_recipes.html", recipe=recipe, categories=categories)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """
    This is the delete recipe functionality
    """
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("get_recipes"))


@app.route("/get_categories")
def get_categories():
    """
    This is the categories functionality for admins
    """
    categories = list(mongo.db.categories.find().sort("category.name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """
    This is the adding categories function for administration
    """
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    """
    This is the editing categories function for administration
    """
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))
    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    """
    This is the delete categories function for administration
    """
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))

# This tells the app how and where to run the application


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            # make sure to turn this to false for submission
            debug=True)
