from flask import Flask, render_template
from logic import get_hangover

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result/<int:drinks>")
def result(drinks):
    verdict, recc = get_hangover(drinks)
    return f"Verdict: {verdict} <br> Recommendations: {', '.join(recc)}"

