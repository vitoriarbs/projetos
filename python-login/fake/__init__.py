from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#criando o site
app = Flask(__name__)

#conectando com o mysql
conexao = 'mysql+pymysql://root:vitoriah100@localhost/fake'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
db = SQLAlchemy(app)

from fake import routes