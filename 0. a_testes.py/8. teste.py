import os

os.system("clear") # Limpa o Terminal.

print('\t====tabuada====')
numero = int(input("Digite um numero: "))
print('\n Tabuada de', numero, ':')
for i in range(1, 1001):
    print(numero, 'X', i, '=', (numero * i))