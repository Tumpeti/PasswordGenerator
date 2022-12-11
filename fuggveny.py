import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E',
           'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

pw_letters = []
pw_numbers = []
pw_symbols = []


def letter_randomizer(nr_letters):
    for letter in range(0, nr_letters):
        letter = letters[random.randint(0, len(letters)-1)]
        pw_letters.append(letter)
    print(pw_letters)


def symbols_randomizer(nr_symbols):
    for symbol in range(0, nr_symbols):
        symbol = symbols[random.randint(0, len(symbols)-1)]
        pw_symbols.append(symbol)
    print(pw_symbols)


def number_randomizer(nr_numbers):
    for number in range(0, nr_numbers):
        number = random.randint(0, len(numbers)-1)
        pw_numbers.append(number)
    print(pw_numbers)


def order_randomizer():
    password = ""

    while len(pw_numbers) != 0 or len(pw_letters) != 0 or len(pw_symbols) != 0:
        list_chooser = random.randint(0, 2)
        if list_chooser == 0 and len(pw_letters) != 0:
            item_chooser = random.randint(0, len(pw_letters) - 1)
            password += pw_letters[item_chooser]
            del (pw_letters[item_chooser])

        elif list_chooser == 1 and len(pw_numbers) != 0:
            item_chooser = random.randint(0, len(pw_numbers) - 1)
            password += str(pw_numbers[item_chooser])
            del (pw_numbers[item_chooser])

        elif list_chooser == 2 and len(pw_symbols) != 0:
            item_chooser = random.randint(0, len(pw_symbols) - 1)
            password += pw_symbols[item_chooser]
            del(pw_symbols[item_chooser])

    print(password)
