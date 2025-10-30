from flask import Blueprint, render_template, Flask, render_template, request, redirect, url_for, session
from .utils import *

bp = Blueprint('main', __name__)


@bp.route('/', methods=["GET", "POST"])
def index():
    guesses = session.get('guesses', [])
    return render_template('index.html', guesses=guesses)


@bp.route("/guess", methods=["POST"])
def guess():
    action = request.form.get("action")
    if action == "restart":
        session['guesses'] = []
        return render_template("index.html", guesses=[])
    guess = request.form.get("guess")
    handle_guess(guess)
    guesses = session.get('guesses', [])
    guesses.append(guess)
    session['guesses'] = guesses
    return render_template("index.html", guesses=guesses)
