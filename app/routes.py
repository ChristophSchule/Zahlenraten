from flask import Blueprint, render_template, Flask, render_template, request, redirect, url_for, session
from .utils import *

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
        return render_template("game_over.html", guesses=guesses, number_to_guess=number_to_guess)
    else:
        return render_template("index.html", guesses=guesses, number_to_guess=number_to_guess)


def start_game():
    session['guesses'] = []
    # Generate a random number between 0 and 100 and store in session
    session['number_to_guess'] = generate_random_number(0, 100)
    session['number_of_attempts'] = 0
    return render_template("index.html", guesses=[], number_to_guess=session['number_to_guess'])
