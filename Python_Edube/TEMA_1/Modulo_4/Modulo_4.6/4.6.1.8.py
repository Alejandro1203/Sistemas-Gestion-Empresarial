dictionary = {"gato" : "chat", 
              "perro" : "chien", 
              "caballo" : "cheval"}

dictionary['gato'] = 'minou'
print(dictionary)

dictionary['cisne'] = 'cygne'
print(dictionary)

dictionary.update({"pato": "canard"})
print(dictionary)

del dictionary["perro"]
print(dictionary)

dictionary.popitem()
print(dictionary) 