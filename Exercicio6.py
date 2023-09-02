'''
Escreva um programa que pergunte em qual mês estamos (1-12) e ao final utilize uma
estrutura de decisão por seleção para escrever o nome do mês por extenso na tela.
'''

numero_mes = int(input("Digite o número do mês (1-12): "))

if numero_mes == 1:
    nome_mes = "Janeiro"
elif numero_mes == 2:
    nome_mes = "Fevereiro"
elif numero_mes == 3:
    nome_mes = "Março"
elif numero_mes == 4:
    nome_mes = "Abril"
elif numero_mes == 5:
    nome_mes = "Maio"
elif numero_mes == 6:
    nome_mes = "Junho"
elif numero_mes == 7:
    nome_mes = "Julho"
elif numero_mes == 8:
    nome_mes = "Agosto"
elif numero_mes == 9:
    nome_mes = "Setembro"
elif numero_mes == 10:
    nome_mes = "Outubro"
elif numero_mes == 11:
    nome_mes = "Novembro"
elif numero_mes == 12:
    nome_mes = "Dezembro"
else:
    nome_mes = "Mês inválido"

# Exiba o nome do mês na tela
print(f"O mês correspondente ao número {numero_mes} é {nome_mes}.")
