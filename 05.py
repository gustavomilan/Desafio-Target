
'''5) Escreva um programa que inverta os caracteres de um string.'''

def invereter(s):
    return s[::-1]


string = "Target"
string_invertida = invereter(string)
print(f"A string invertida de '{string}' é '{string_invertida}'.")