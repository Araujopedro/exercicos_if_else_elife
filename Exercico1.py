#Escreva um algoritmo que pergunte o valor de uma mercadoria e qual o
# valor que o usuário tem em mãos e diga se o dinheiro é ou não é suficiente para adquirir esta mercadoria;

num= input("digite o valor da mercadoria:")
num2= input("digite o valor que o usuario tem em mãos:")

if num2>=num:
    print("voce tem o valor suficiente para efetuar a compra")
else:
    print("voce não tem o valor para efetuar a compra")


