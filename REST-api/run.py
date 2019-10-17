from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS


app = Flask(__name__)
api = Api(app)
CORS(app)

import urllib
import pyodbc
params = urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=YAMI;DATABASE=Automalogica-challenge;Trusted_Connection=yes;')
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params

app.config['SECRET_KEY'] = 'Automalogica-Challenge'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()


app.config['JWT_SECRET_KEY'] = 'AiesecIsPeople'
jwt = JWTManager(app)

from models import user
from resources import userResources

api.add_resource(userResources.UserRegistration, '/signup')
api.add_resource(userResources.UserLogin, '/login')
api.add_resource(userResources.SecretResource, '/home')

api.add_resource(userResources.TokenRefresh, '/token/refresh')
