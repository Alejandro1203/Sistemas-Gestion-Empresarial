dictionary = {"gato" : "chat", 
              "perro" : "chien", 
              "caballo" : "cheval"}

phone_number = {"jefe" : 1234567, 
                "lacayo" : 7875634}

empty_dictionary = {}

print(dictionary["gato"])
# print(phone_number['presidente'])

words = ['gato', 'león', 'caballo']

for word in words:
    if word in dictionary:
        print(word, "-->", dictionary[word])
    else:
        print(word, "no tá")