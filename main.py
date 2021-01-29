MIN_LENGTH = 8
MAX_LENGTH = 32
DEFAULT_CHARACTERS = "abcdefghijklmnopqrstuvwxyz"

import random

def generate_password(info):
    password = ""

    for _ in range(info["length"]):
        random_character = random.choice(info["characters"])

        if info["includes_uppercase_characters"] == True and (round(random.random()) == 1):
            random_character = random_character.upper()

        password = password + random_character

    return password

def get_characters():
    return list(DEFAULT_CHARACTERS)

def get_choice_of_including_uppercase_characters():
    while True:
        input_text = input("Include uppercase characters? (Y/N): ")
        if input_text.lower() == "y":
            return True
        elif input_text.lower() == "n":
            return False
        else:
            continue

def get_length():
    while True:
        desired_length = input("Enter desired length of password: ")
    
        try:
            desired_length = int(desired_length)
        except ValueError:
            continue

        if not isinstance(desired_length, int):
            continue
        elif desired_length < MIN_LENGTH or desired_length > MAX_LENGTH:
            continue

        return desired_length

def main():
    password = generate_password({
        "length": get_length(),
        "includes_uppercase_characters": get_choice_of_including_uppercase_characters(),
        "characters": get_characters(),
    })

    print(password)

    """
    has_symbols = True
    has_numbers = True
    includes_lowercase_characters = True
    includes_uppercase_characters = True
    includes_similar_characters = True
    includes_anbiguous_characters = True
    """

if (__name__ == "__main__"):
    main()