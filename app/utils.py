from flask import session

def generate_random_number(start, end):
    import random

    return random.randint(start, end)


def handle_guess(guess):
    number_to_guess = session.get("number_to_guess")
    if number_to_guess is None:
        return "No number to guess set."
    try:
        guess_int = int(guess)
    except (ValueError, TypeError):
        return "Invalid guess."
    if guess_int == number_to_guess:
        return "correct"
    elif guess_int < number_to_guess:
        return "too low"
    else:
        return "too high"