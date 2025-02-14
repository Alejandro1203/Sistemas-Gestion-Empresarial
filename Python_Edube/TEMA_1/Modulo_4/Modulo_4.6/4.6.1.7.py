dictionary = {"gato" : "chat", 
              "perro" : "chien", 
              "caballo" : "cheval"}

for spanish, french in dictionary.items():
    print(spanish, "-->", french)

for french in sorted(dictionary.values()):
    print(french)