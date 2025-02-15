def crypt_caesar(strng):
    if not isinstance(strng, str):
        return "No es una cadena loco"
    else:
        cipher = ''
    
        for char in strng:
            if not char.isalpha():
                continue

            char = char.upper()
            code = ord(char) + 1

            if(code > ord('Z')):
                code = ord('A')
    
            cipher += chr(code)
        
        return cipher

print(crypt_caesar(input("Introduce un mensaje: ")))



