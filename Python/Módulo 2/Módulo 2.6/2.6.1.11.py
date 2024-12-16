hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

mins += dura
hour += mins // 60
dias = hour
hour %= 24
mins %= 60 
dias = dura // 1440


print(str(hour) + ":" + str(mins))
print("Días: " + str(dias))