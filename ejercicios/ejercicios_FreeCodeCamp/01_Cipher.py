# programa que imprime un texto e indica en qué posición del alfabeto está cada letra

text = 'Hello World'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for char in text.lower():
    index = alphabet.find(char)
    print(char, index)