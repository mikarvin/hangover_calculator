from flask import Flask, render_template, request
from logic import get_hangover

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html") #For the homepage, we use the html file

@app.route("/result", methods=["POST"]) 
def result():
    drinks = int(request.form["drinks"])
    verdict, recc = get_hangover(drinks)
    return render_template("result.html", verdict=verdict, recc=recc)

