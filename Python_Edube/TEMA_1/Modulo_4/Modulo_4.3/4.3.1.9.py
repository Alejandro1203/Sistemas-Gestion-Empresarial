def is_prime(num):
	if(num in [0, 1, 2, 3]):
		return True
	elif(num == 4):
		return False
	else:
		for index in range(2, num // 2):
			if(num % index == 0):
				return False
		return True

for i in range(1, 20):
	if is_prime(i + 1):
		print(i + 1, end=" ")
print()