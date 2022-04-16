from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField
from wtforms.validators import InputRequired, DataRequired
from flask_wtf.file import FileRequired, FileAllowed
from wtforms.widgets import TextArea

image_types = ['jpg', 'png', 'jpeg', 'gif', 'svg', 'webp']

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class UserForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    biography = StringField('Biography', validators=[DataRequired()], widget=TextArea())
    photo = FileField('File', validators=[FileAllowed(image_types, 'Image only!'), FileRequired('File was empty!')])

class CarForm(FlaskForm):
    description = StringField('Description', validators=[DataRequired()])
    make= StringField('Description', validators=[DataRequired()])
    model = StringField('Description', validators=[DataRequired()])
    colour = StringField('Description', validators=[DataRequired()])
    year = StringField('Description', validators=[DataRequired()])
    transmission = StringField('Description', validators=[DataRequired()])
    car_type = StringField('Description', validators=[DataRequired()])
    price = StringField('Description', validators=[DataRequired()])
    photo = FileField('File', validators=[FileAllowed(image_types, 'Image only!'), FileRequired('File was empty!')])
