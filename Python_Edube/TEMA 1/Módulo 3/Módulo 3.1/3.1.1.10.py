cadena = str(input("Cadena: "))

if(cadena == "ESPATIFILO"):
    print("Si, ¡El ESPATIFILO es la mejor planta de todos los tiempos!")
elif(cadena == "espatifilo" or cadena == "Espatifilo"):
    print("No, ¡quiero un gran ESPATIFILIO!")
else: 
    print("!ESPATIFILO!, ¡No ", cadena, "!", sep="")