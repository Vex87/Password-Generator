MIN_LENGTH = 8
MAX_LENGTH = 32
DEFAULT_CHARACTERS = "abcdefghijklmnopqrstuvwxyz"
DEFAULT_NUMBERS = "0123456789"

import random

def generate_password(info):
    password = ""

    for _ in range(info["length"]):
        random_character = random.choice(info["characters"])

        if info["includes_uppercase_characters"] == True and (isinstance(random_character, str)) and (round(random.random()) == 1):
            random_character = random_character.upper()

        password = password + str(random_character)

    return password

def get_characters():
    characters = list(DEFAULT_CHARACTERS)
    if DEFAULT_NUMBERS:
        characters.extend(list(DEFAULT_NUMBERS))
    
    return characters

def get_boolean_choice(text):
    while True:
        input_text = input(f"{text} (Y/N): ")
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
        "includes_uppercase_characters": get_boolean_choice("Include uppercase characters?"),
        "has_numbers": get_boolean_choice("Include numbers?"),
        "characters": get_characters(),
    })

    print(f"GENERATED PASSWORD: {password}")

    """
    has_symbols = True
   
    includes_lowercase_characters = True
    includes_uppercase_characters = True
    includes_similar_characters = True
    includes_anbiguous_characters = True
    """

if (__name__ == "__main__"):
    main()