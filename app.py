from flask import Flask, render_template   # procura por um template, .html, na pasta templates

def create_app():
    app = Flask(__name__)  # represento o arquivo atual

    @app.route('/') # pagina padrão
    def home():
        return render_template("home.html") 

    @app.route("/salvador")
    def salvador():
        return "Salvador é a capital da Bahia"
    
    return app