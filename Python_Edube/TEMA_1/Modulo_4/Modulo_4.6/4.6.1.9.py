school_class = {}

while True:
    name = input("Ingresa el nombre de un estudiante: ")

    if name == '':
        break

    score = int(input("Ingresa una calificación[0-10]: "))
    if score not in range(0, 11):
        break

    if name in school_class:
        school_class[name] += (score, )
    else:
        school_class[name] = (score, )

for name in sorted(school_class.keys()):
    adding = 0
    counter = 0

    for score in school_class[name]:
        counter += 1
        adding += score

    print(name, "media -->", adding / counter)