def sum_num_str(strng):
    if not isinstance(strng, str):
        return "No es una cadena mi loco"
    else:
        strng = strng.split()
        sum = 0

        for char in strng:

            if char.isalpha():
                continue

            sum += float(char)
        
        return sum
    
print(sum_num_str("1 2 3 4 5 w 6"))

