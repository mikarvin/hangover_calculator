from flask import Flask, render_template, request, redirect
from logic import calculate_score, get_hangover

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html") #For the homepage, we use the html file

@app.route("/result", methods=["GET", "POST"]) 
def result():
    if request.method == "GET":
        return redirect("/")
    #Drinks fields
    beers = int(request.form["beers"])
    shots = int(request.form["shots"])
    cocktails = int(request.form["cocktails"])
    wines = int(request.form["wines"])
    #Score calc
    score = calculate_score(beers, shots, cocktails, wines) #Calculate score based on num of drinks
    #Verdict and recommendations
    verdict, recc = get_hangover(score) #pass it back to logic page to get_hangover function

    return render_template("result.html", verdict=verdict, recc=recc)

