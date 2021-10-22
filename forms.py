"""Form object declaration."""
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SelectField, IntegerField, FormField, Form, FieldList
from wtforms.validators import DataRequired,  InputRequired, NumberRange, Optional


category_name_list = [('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Snacks', 'Snacks')]


class Preparations(Form):
    # preparation form for recipes
    step = TextAreaField('Preparation step', validators=[InputRequired()])


class InsertRecipeForm(FlaskForm):
    # insert recipe form for adding or editing new recipe to database
    recipe_name = StringField('Recipe name', validators=[InputRequired()])
    category_name = SelectField(
        'Category', choices=category_name_list, validators=[DataRequired()])
    preparation_time = IntegerField(
        'Preparation time (minutes)', validators=[
            DataRequired(), NumberRange(min=5, max=180)])
    portions = IntegerField(
        'Amount of portions', validators=[
            DataRequired(), NumberRange(min=1, max=6)])
    recipe_description = TextAreaField(
        'Recipe description', validators=[Optional()])
    preparation = FieldList(FormField(Preparations), min_entries=1)
    recipe_image = FileField('Recipe picture')
