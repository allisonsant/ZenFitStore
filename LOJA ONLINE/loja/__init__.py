from flask import Flask
from flask_pymongo import PyMongo
from werkzeug.utils import secure_filename
from flask_uploads import IMAGES, UploadSet, configure_uploads

from flask_bcrypt import Bcrypt
from werkzeug.wrappers import Request  # Importando Request do local correto
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'ZenFitStore'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/ZenFitStore'
app.config['SECRET_KEY'] = 'senhasecreta'
mongo = PyMongo(app)
bcrypt = Bcrypt(app)

app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

from loja.admin import rotas
from loja.produtos import rotas


# Agora você pode usar o objeto `mongo` para interagir com o MongoDB
# Por exemplo:
# colecao = mongo.db.nome_da_sua_colecao
# colecao.insert_one({'chave': 'valor'})



