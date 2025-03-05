
# projekt_1.py: první projekt do Engeto Online Python Akademie

# author: Pavel Nováček
# email: gippel@seznam.cz

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30 and the Union Pacific Railroad,
which traverse the valley. ''',
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

registered_users = dict(
    bob = "123",
    ann = "pass123",
    mike = "password123",
    liz = "pass123"
)

# Kontrola registrace uživatele
user_name = input("Enter your username: ")

if user_name in registered_users:
    user_password = input("Enter your password: ")
    if registered_users.get(user_name) == user_password:
        print("username:", user_name,
            "\npassword:", user_password,
            "\n" + "-" * 41,
            "\nWelcome to the app,", user_name,
            "\nWe have", len(TEXTS), "texts to be analyzed.",
            "\n" + "-" * 41,
            )
    else:
        print("username:", user_name,
            "\npassword:", user_password,
            "\nwrong password, terminating the program.."
            )
        exit()
else:
    print("username:", user_name,       
        "\nunregistered user, terminating the program..")
    exit()

# Výběr textu
try:
    text_choice = int(input(f"Enter a number btw. 1 and {len(TEXTS)} to select: "))
    0 < text_choice <= len(TEXTS)   
except ValueError:
    print("Invalid input. Enter A NUMBER within the range.")
    exit()    
else:
    text_choice -= 1 
    if text_choice in range(len(TEXTS)):
        text_choice = TEXTS[text_choice] 
    else: 
        print("Number out of range")
        exit()          

# # Počet slov
text_list = text_choice.replace(",", " ").replace(".", " ").split()
title_case_words = 0
upper_case_words = 0
lower_case_words = 0 
numeric = 0
numeric_count = 0
word_length_list = []

for word in text_list:
    if word.isupper(): 
        upper_case_words += 1
    elif word.istitle(): 
        title_case_words += 1    
    elif word.islower(): 
        lower_case_words += 1
    elif word.isnumeric(): 
        numeric += 1
        numeric_count += int(word)

    word_length_list.append(len(word))

print("-" * 41)
print(f"There are {len(text_list)} words in the selected text.")
print(f"There are {title_case_words} titlecase words.")
print(f"There are {upper_case_words} uppercase words.")
print(f"There are {lower_case_words} lowercase words.")
print(f"There are {numeric} numeric strings.")
print(f"The sum of all the numbers {numeric_count}")
print("-" * 41)

# Délka slov
print("LEN|     OCCURENCES     |NR.")
print("-" * 41)

maximum = max(word_length_list) + 1

for number in range(1, maximum):
    quantity = word_length_list.count(number) 
    if len(str(number)) > 1:
        space = " " 
    else:
        space = " " * 2 
    print(f"{space}{number}|{'*' * quantity + ' ' * (20 - quantity)}|{quantity}")
    




