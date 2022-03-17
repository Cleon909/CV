from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

UPLOAD_FOLDER = 'application/static'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:todo@db/analytics.db'
app.config['SECRET_KEY'] = 'serfser'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

from application import routes