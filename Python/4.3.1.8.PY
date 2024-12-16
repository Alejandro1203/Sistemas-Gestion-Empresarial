def is_year_leap(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        #print("Año" + str(year) + " es bisiesto: " + str(True))
        return True

def days_in_month(year, month):
    if(month in [1, 3, 5, 7, 8, 10, 12]):
        return 31
    elif(is_year_leap(year) and month == 2):
        return 29
    elif(not is_year_leap(year) and month == 2):
        return 28
    else:
        return 30

def day_of_year(year, month, day):

    if(year < 0 or (month < 1 or month > 12) or (day < 1 or day > 31) or day > days_in_month(year, month)):
        return None
    else:
        days = 0

        for i in range(1, month):
            days += days_in_month(year, i)
    
        days += day

    return days


print(day_of_year(2000, 12, 31))
print(day_of_year(2000, 1, 1))
print(day_of_year(2000, 13, 1))
print(day_of_year(2000, 1, 41))