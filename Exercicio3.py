'''
Escreva um algoritmo que verifique se um número inteiro digitado pelo usuário é ou não divisível por 5
'''

Num1=int(input("digite um numero:"))

div= Num1 % 5

if div <=0:
    print(f"o valor é divisivel,o resto da divisão é ={div}")

else:
    print(f"o valor não é divisivel, o resto da divisão é {div}")

