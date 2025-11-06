from flask import Blueprint, render_template, Flask, render_template, request, redirect, url_for, session
from .utils import *
from .models import User
from . import db

bp = Blueprint('main', __name__)


@bp.route('/', methods=["GET", "POST"])
def index():
    return start_game()



@bp.route("/guess", methods=["POST"])
def guess():
    action = request.form.get("action")
    if action == "restart":
        return start_game()
    guess = request.form.get("guess")
    result = handle_guess(guess)
    guesses = session.get('guesses', [])
    guesses.append(guess)
    session['guesses'] = guesses
    number_to_guess = session.get('number_to_guess')
    if result == "correct":
        points = session.get('guesses').__len__()
        save_score('Test', points)
        scores = load_scores()
        return render_template("game_over.html", guesses=guesses, number_to_guess=number_to_guess,  scores=scores)
    else:
        scores = load_scores()
        return render_template("index.html", guesses=guesses, result=result,  scores=scores)


def start_game():
    session['guesses'] = []
    # Generate a random number between 0 and 100 and store in session
    session['number_to_guess'] = generate_random_number(0, 100)
    session['number_of_attempts'] = 0
    scores = load_scores()
    return render_template("index.html", guesses=[], scores=scores)

def load_scores():
    users = User.query.order_by(User.points.asc(),User.date_created.asc()).limit(10).all()
    return users

def save_score(username, points):
    user = User(username=username, points=points)
    db.session.add(user)
    db.session.commit()