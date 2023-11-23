from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def get_database_uri():
    user = 'root'
    password = 'eggh-22cgFb-gBg4aH6DfFAC14edeFC6'
    db_name = 'railway'
    host = 'viaduct.proxy.rlwy.net'
    port = 51991

    return f'mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}'


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = get_database_uri()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app import routes