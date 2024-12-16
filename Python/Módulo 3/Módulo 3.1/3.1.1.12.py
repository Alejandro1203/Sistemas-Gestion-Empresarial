year = int(input("Introduce un año:"))

if(year % 4 != 0):
    print("Año común")
elif(year % 100 != 0):
    print("Año bisiesto")
elif(year % 400 != 0):
    print("Año común")
else:
    print("Año bisiesto")