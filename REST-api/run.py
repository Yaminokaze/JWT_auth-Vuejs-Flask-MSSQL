from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)

import urllib
import pyodbc
#params = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 10.0};SERVER=dagger;DATABASE=test;UID=user;PWD=password")
#params = urllib.parse.quote_plus("driver='{SQL Server}';Server=localhost;database=Automalogica-challenge;Trusted_Connection=True;")
#driver = 'ODBC+DRIVER+17+for+SQL+Server'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://YAMI/Automalogica-challenge'
#"mssql+pyodbc://%s:%s@%s/%s?driver=%s" % ("YAMI", "", "localhost", "Automalogica-challenge", driver )
#"mssql+pyodbc:///?odbc_connect=%s" % params

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
