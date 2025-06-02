from flask import Flask
from .routes import bp

app = Flask(__name__, template_folder='validator/app/templates')
app.register_blueprint(bp)

#Configurando a rota para servir o index.html
@app.route('/')
def index():
    return app.send_static_file('index.html')