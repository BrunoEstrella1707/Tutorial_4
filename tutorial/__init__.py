from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///aplicacao.db"
app.config['SECRET_KEY'] = '52a457659963e0b68ed35a11'
db.init_app(app)

from tutorial import routes