from flask import Blueprint

# Criando o Blueprint
main = Blueprint('main', __name__)

# Importando as rotas
from app.main import routes