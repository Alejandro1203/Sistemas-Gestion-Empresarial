def display_digits(digits):
    segments = {
        '0': ["###", "# #", "# #", "# #", "###"],
        '1': ["  #", "  #", "  #", "  #", "  #"],
        '2': ["###", "  #", "###", "#  ", "###"],
        '3': ["###", "  #", "###", "  #", "###"],
        '4': ["# #", "# #", "###", "  #", "  #"],
        '5': ["###", "#  ", "###", "  #", "###"],
        '6': ["###", "#  ", "###", "# #", "###"],
        '7': ["###", "  #", "  #", "  #", "  #"],
        '8': ["###", "# #", "###", "# #", "###"],
        '9': ["###", "# #", "###", "  #", "###"]
    }
    
    lines = ["", "", "", "", ""]
    
    for digit in digits:
        if digit in segments:
            for i in range(5):
                lines[i] += segments[digit][i] + " "
        else:
            print("Dígito no válido")
            return
    
    for line in lines:
        print(line)

# Ejemplo de uso
display_digits('123')
display_digits('9081726354')