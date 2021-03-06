from flask import Flask
from config import Configuration
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_admin import Admin

ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__, static_folder='static')
app.config.from_object(Configuration)

db = SQLAlchemy(app)
login_manager = LoginManager(app)

mail = Mail(app)

admin = Admin(app)