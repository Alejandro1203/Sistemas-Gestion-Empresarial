user_word = input("Ingrese una palabra: ")
user_word = user_word.upper()

for letter in user_word:

    if(letter != "A" and letter != "E" and letter != "I" and letter != "O" and letter != "U"):
        print(letter)