def generate_random_number(start, end):
    import random
    return random.randint(start, end)

def start_game(start, end):
    number_to_guess = generate_random_number(start, end)
    attempts = 0

def handle_guess(guess):
    print(f"Guess received: {guess}")
    return "Function executed!"