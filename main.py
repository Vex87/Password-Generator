MIN_LENGTH = 8
MAX_LENGTH = 32
DEFAULT_LETTERS = "abcdefghijklmnopqrstuvwxyz"
DEFAULT_NUMBERS = "0123456789"
DEFAULT_ANBIGUOUS_CHARACTERS = "_!#^*$%"

import random
from colorama import Fore, Style

def generate_password(info):
    get_characters(info)
    password = ""

    for _ in range(info["length"]):
        random_character = random.choice(info["characters"])
        password = password + str(random_character)

    return password

def get_characters(info):
    characters = list(DEFAULT_LETTERS)

    if info["includes_uppercase_characters"]:
        for letter in list(DEFAULT_LETTERS):
            characters.append(letter.upper())
    if info["has_numbers"]:
        characters.extend(list(DEFAULT_NUMBERS))
    if info["has_anbiguous_characters"]:
        characters.extend(list(DEFAULT_ANBIGUOUS_CHARACTERS))
    
    info["characters"] = characters

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
    while True:
        password = generate_password({
            "length": get_length(),
            "includes_uppercase_characters": get_boolean_choice("Include uppercase characters?"),
            "has_numbers": get_boolean_choice("Include numbers?"),
            "has_anbiguous_characters": get_boolean_choice("Include anbiguous characters?"),
            "characters": []
        })

        print(Fore.GREEN + password)
        print(Style.RESET_ALL) 

if (__name__ == "__main__"):
    main()