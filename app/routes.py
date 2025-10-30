from flask import Blueprint, render_template, Flask, render_template, request, redirect, url_for
from .utils import *

bp = Blueprint('main', __name__)

@bp.route('/', methods=["GET", "POST"])
def index():
    guess = request.form.get("guess")  # or None if GET
    return render_template('index.html', guess=guess)

@bp.route("/guess", methods=["POST"])
def guess():
    # get the value from the form
    guess = request.form.get("guess")
    handle_guess(guess)  
    return render_template("index.html", guess=guess)
