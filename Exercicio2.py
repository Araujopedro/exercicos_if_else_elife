#Um estacionamento cobra R$ 5,00 por hora porém possui um teto de
# cobrança máxima de R$ 35,00, independente do número de horas.
# Escreva um algoritmo que pergunte ao usuário qual foi
# o período de permanência em horas e escreva na tela o total a pagar.

PP=int(input("periodo de permanencia:"))

Val= PP*5

if Val<=35:
    print(f"voce tem que pagar {Val}")

elif Val>=35:
    print(f"total a pagar é de 35")
