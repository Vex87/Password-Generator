MIN_LENGTH = 8
MAX_LENGTH = 32
DEFAULT_CHARACTERS = "abcdefghijklmnopqrstuvwxyz"

import random

def generate_password(info):
    password = ""

    for _ in range(info["length"]):
        random_character = random.choice(info["characters"])
        password = password + random_character

    return password

def get_characters():
    return list(DEFAULT_CHARACTERS)

def get_length():
    desired_length = None

    while not desired_length:
        desired_length = input("Enter desired length of password: ")
    
        try:
            desired_length = int(desired_length)
        except ValueError:
            desired_length = None
            continue

        if not isinstance(desired_length, int):
            desired_length = None
            continue
        if desired_length < MIN_LENGTH or desired_length > MAX_LENGTH:
            desired_length = None
            continue

    return desired_length

def main():
    password = generate_password({
        "length": get_length(),
        "characters": get_characters()
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