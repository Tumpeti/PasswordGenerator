# Password Generator Project
import fuggveny

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

fuggveny.letter_randomizer(nr_letters)
fuggveny.symbols_randomizer(nr_symbols)
fuggveny.number_randomizer(nr_numbers)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

fuggveny.order_randomizer()
