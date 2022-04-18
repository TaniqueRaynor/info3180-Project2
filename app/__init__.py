from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_wtf.csrf import CSRFProtect
app = Flask(__name__)
app.config.from_object(Config)

"""
after 'flask db init' creates migrations folder go to env.py and add -> 'from app.models import *'
then 'flask db migrate'
then 'flask db upgrade'
"""


db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from flask_migrate import Migrate
migrate = Migrate(app, db)

from app import views
csrf = CSRFProtect(app)