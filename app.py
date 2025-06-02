from flask import Flask, render_template
from validator.app.routes import bp 

app = Flask(__name__, template_folder='validator/app/templates')
app.register_blueprint(bp)


@app.route("/")
def home():
    return render_template("index.html")
