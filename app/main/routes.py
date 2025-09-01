from app.main import main

@main.route('/')
def index():
    return "Olá, Mundo!"

@main.route('/sobre')
def sobre():
    return "Olá, João!"