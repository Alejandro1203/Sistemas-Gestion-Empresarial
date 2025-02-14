dictionary = {"gato" : "chat", 
              "perro" : "chien", 
              "caballo" : "cheval"}

for keys in dictionary.keys():
    print(keys, "-->", dictionary[keys])

for keys in sorted(dictionary.keys()):
    print(keys, "-->", dictionary[keys])