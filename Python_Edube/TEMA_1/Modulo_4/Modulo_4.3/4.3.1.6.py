def is_year_leap(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("Año", year, "es bisiesto:",True)
        return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end=" ")
	result = is_year_leap(yr)
	
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")