from flask import Flask, render_template, redirect

import random

app = Flask(__name__)

RANGE = 101
def random_num():
    random_number = random.randint(0, RANGE-1)
    return random_number

correct = 0

@app.get("/")
def index():
    global correct
    correct = random_num()
    return render_template("index.html")

@app.get("/game")
def game():
    return render_template("game.html", Range=RANGE)

@app.get("/guess/<int:num>")
def isCorrect(num):
    while num != correct:
        if num > correct:
            message = "High"
            return render_template('guess.html', message=message)
        elif num < correct:
            message = "Low"
            return render_template('guess.html', message=message)

    message = f"Correct. The number is {num}"
    return render_template('guess.html', message=message)