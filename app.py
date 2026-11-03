from flask import Flask
from logic import get_hangover

app = Flask(__name__)


@app.route("/")
def home():
    return "Hangover Calculator coming soon 🍺"

@app.route("/result/<int:drinks>")
def result(drinks):
    verdict, recc = get_hangover(drinks)
    return f"Verdict: {verdict} <br> Recommendations: {', '.join(recc)}"

