# """
# projekt_1.py: první projekt do Engeto Online Python Akademie
# author: Jiří Nágl
# email: nagl.jirka@seznam.cz
# discord: jirkanagl
# """

import sys
from task_template import TEXTS


users = {"user1" : {"user" : "bob", "password" : "123"},
         "user2" : {"user" : "ann" , "password" : "pass123"},
         "user3" : {"user" : "mike", "password" : "password123"},
         "user4" : {"user" : "liz", "password" : "pass123"}
         }
user_input = input("user:")
password_input = input("password:")
print(40 * "-")


for user, name in users.items():
    if name["user"] == user_input and name["password"] == password_input:
        print("Welcome to the app,", name["user"])
        print("We have 3 texts to be analyzed.")
        break

else:
    print("username:", user_input)
    print("password:", password_input)
    print("unregistered user, terminating the program..")
    sys.exit()
    

text_input = input("Enter a number btw. 1 and 3 to select:")
if not text_input.isnumeric():
    print("username:", user_input)
    print("password:", password_input)
    print("wrong input, terminating the program..")
    sys.exit()


text_index = int(text_input) - 1

index_list = list(range(len(TEXTS) + 1))
if int(text_input) in index_list:
    text_index = int(text_input) - 1
    # počet slov
    count_words = len(TEXTS[text_index].split())

    count_upletter = 0
    count_uppercase_words = 0
    count_lowercase_words = 0
    count_numeric_str = 0
    sum_numbers = []

    for word in TEXTS[text_index].split():
        # počet slov začínajících velkým písmenem
        if word.istitle():
            count_upletter += 1

        # počet slov psaných velkými písmeny
        if word.isupper() and word.isalpha():
            count_uppercase_words += 1

        # počet slov psaných malými písmeny
        if word.islower():
            count_lowercase_words += 1

         # počet čísel
        if word.isnumeric():
            count_numeric_str += 1

        # suma všech čísel
        if word.isnumeric():
            sum_numbers.append(int(word))

    print("There are", count_words, "words in the selected text.")
    print("There are", count_upletter, "titlecase words.")
    print("There are", count_uppercase_words, "uppercase words.")
    print("There are", count_lowercase_words, "lowercase words.")
    print("There are", count_numeric_str, "numeric strings.")
    print("The sum of all the numbers", sum(sum_numbers))

    print("-" * 40)
    
    # sloupcový graf četnosti délek slov
    words_length = []
    key = {}
    for word in TEXTS[text_index].split():
        clean_word = word.strip(".,")
        length = len(clean_word)
        words_length.append(length)

    print("LEN" + "|" + "OCCURENCES".center(20) + "|" + "NR.")
    print("-" * 40)

    for number in words_length:
        if number not in key:
            key[number] = 1
        else:
            key[number] = key[number] + 1
    for key, value in sorted(key.items()):
        print(str(key).rjust(2), "|" + ("*" * value).ljust(20) + "|", value)
    

else:
    print("username:", user_input)
    print("password:", password_input)
    print("wrong input, terminating the program..")
    sys.exit()

    
