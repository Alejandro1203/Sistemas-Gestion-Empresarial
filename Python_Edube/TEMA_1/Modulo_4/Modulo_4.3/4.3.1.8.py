def is_year_leap(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("Año", year, "es bisiesto:",True)
        return True

def days_in_month(year, month):
    if(month == 2 and is_year_leap(year)):
          return 29
    elif(month == 2 and not is_year_leap(year)):
          return 28
    elif(month in [1, 3, 5, 7, 8, 10, 12]):
          return 31
    else:
          return 30

def day_of_year(year, month, day):
    sum = 0

    for index in range(1, month):
        sum += days_in_month(year, index)

    return sum+day

print(day_of_year(2000, 12, 31))