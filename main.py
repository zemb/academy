# projekt_1.py: první projekt do Engeto Online Python Akademie

"""
author: Martin Žember
email: zember@gmail.com
"""

# Předpřipravené texty
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

# Registrovaní uživatelé
REGISTERED_USERS = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Pomocné funkce


def analyze_text(text):
    """Analyzuje text a vrací statistiky."""
    words = text.split()
    num_words = len(words)
    num_titlecase = sum(1 for word in words if word.istitle())
    num_uppercase = sum(1 for word in words if word.isupper())
    num_lowercase = sum(1 for word in words if word.islower())
    num_numbers = sum(1 for word in words if word.isdigit())
    sum_numbers = sum(int(word) for word in words if word.isdigit())

    # Slovník pro každou možnou (nalezenou) délku
    word_lengths = {}
    word_lengths_max = 0
    for word in words:
        length = len(word.strip(".,"))
        if length not in word_lengths:
            word_lengths[length] = 0
        word_lengths[length] += 1
        # Dřevní implementace max()
        if word_lengths_max < word_lengths[length]:
            word_lengths_max = word_lengths[length]

    return {
        "num_words": num_words,
        "num_titlecase": num_titlecase,
        "num_uppercase": num_uppercase,
        "num_lowercase": num_lowercase,
        "num_numbers": num_numbers,
        "sum_numbers": sum_numbers,
        "word_lengths": word_lengths,
        "word_lengths_max": word_lengths_max
    }

# Hlavní kód


def main():
    num_texts = len(TEXTS)
    if not num_texts:
        print("Odd. No texts to analyze. Terminating the program..")
        return

    print("----------------------------------------")
    username = input("username:")
    password = input("password:")
    print("----------------------------------------")

    # Kontrola přihlašovacích údajů
    if username not in REGISTERED_USERS or REGISTERED_USERS[username] != password:
        print("unregistered user, terminating the program..")
        return

    print(f"Welcome to the app, {username}")
    print(f"We have {num_texts} texts to be analyzed.")
    print("----------------------------------------")

    # Výběr textu
    try:
        text_choice = int(
            input(f"Enter a number btw. 1 and {num_texts} to select: "))
        if text_choice < 1 or text_choice > num_texts:
            raise ValueError
    except ValueError:
        print("Invalid choice, terminating the program..")
        return

    # Analýza vybraného textu
    selected_text = TEXTS[text_choice - 1]
    stats = analyze_text(selected_text)

    # Výstup statistiky
    print("----------------------------------------")
    print(f"There are {stats['num_words']} words in the selected text.")
    print(f"There are {stats['num_titlecase']} titlecase words.")
    print(f"There are {stats['num_uppercase']} uppercase words.")
    print(f"There are {stats['num_lowercase']} lowercase words.")
    print(f"There are {stats['num_numbers']} numeric strings.")
    print(f"The sum of all the numbers {stats['sum_numbers']}")
    print("----------------------------------------")
    # Šířka prostředního sloupce je podle nejdelší hodnoty
    print(f"LEN|{'OCCURENCES':{stats['word_lengths_max']}}|NR.")
    print("----------------------------------------")
    for length, occurrences in sorted(stats['word_lengths'].items()):
        print(
            f"{length:3}|{'*' * occurrences:{stats['word_lengths_max']}}|{occurrences}")


if __name__ == "__main__":
    main()
