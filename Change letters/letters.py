
# Frase  a convertir
text = "Hola, que tal"

# Cree un diccionario con las letras como claves y los reemplazos como valores
replace_dict = {
    'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 
    'g': 't', 'h': 's', 'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o', 
    'm': 'n', 'n': 'm', 'ñ': 'ñ', 'o': 'l', 'p': 'k', 'q': 'j', 
    'r': 'i', 's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 
    'x': 'c', 'y': 'b', 'z': 'a', 
    'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V', 'F': 'U', 
    'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q', 'K': 'P', 'L': 'O', 
    'M': 'N', 'N': 'M', 'Ñ': 'Ñ', 'O': 'L', 'P': 'K', 'Q': 'J', 
    'R': 'I', 'S': 'H', 'T': 'G', 'U': 'F', 'V': 'E', 'W': 'D', 
    'X': 'C', 'Y': 'B', 'Z': 'A'
}


# Usa el diccionario para reemplazar cada letra en la frase
output = ""
for letter in text:
    if letter in replace_dict:
        output += replace_dict[letter]
    else:
        output += letter


# Imprime: "Sloz jfv gzo"
print(output)
