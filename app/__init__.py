from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://suporte:Suporte99@localhost/eventos_v1'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['UPLOAD_PATH'] = os.path.dirname(os.path.abspath(__file__)) + "/static/assets/images/eventos/"

# Importando os módulos com as rotas
from app.controllers import index
from app.controllers import atividades
from app.controllers import eventos
from app.controllers import certificados

# Importando os models
from app.models import tables
