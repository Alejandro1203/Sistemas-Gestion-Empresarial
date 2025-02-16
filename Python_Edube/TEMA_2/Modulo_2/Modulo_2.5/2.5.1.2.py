def descrypt_caesar(cipher):
    if not isinstance(cipher, str):
        return "No es una cadena loco"
    else:    
        text = ''

        for char in cipher:
            if not char.isalpha():
                continue

            char = char.upper()
            code = ord(char) - 1

            if(code < ord('A')):
                code = ord('Z')
            
            text += chr(code)
        
        return text

print(descrypt_caesar(input("Ingresa un pictograma: ")))