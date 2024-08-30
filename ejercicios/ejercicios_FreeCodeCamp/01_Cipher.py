# Programa 'Cifrado de texto'

# Partimos de un programa que imprime un texto e indica en qué posición del alfabeto está cada letra
text = 'Hello World'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for character in text.lower():
    index = alphabet.find(character)
    print(character, index)


# Para llegar al código del cifrado de texto (Cesar):
text = 'Hello World'
shift = 3

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

caesar(text, shift)

# Y un cifrado más completo (Vigenere):
text = 'Hello Wold'
custom_key = 'python'

def vigenere(message, key):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
    
        # Append space to the message
        if char == ' ':
            encrypted_text += char
        else:        
            # Find the right key character to encode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    
    return encrypted_text
    
encryption = vigenere(text, custom_key)
print(encryption)

# Y el programa final:
