'''Considerando o IMC (índice de massa corpórea), calculado como peso/(altura*altura), exiba a situação da pessoa com base na seguinte tabela:

IMC Situação

<= 18.5 Abaixo do peso

>18.5 e <=24.9 Peso ideal

>24.9 Acima do peso'''


peso = float(input("Digite o peso em quilogramas: "))
altura = float(input("Digite a altura em metros: "))


imc = peso / (altura ** 2)


if imc <= 18.5:
    situacao = "Abaixo do peso"
elif imc <= 24.9:
    situacao = "Peso ideal"
else:
    situacao = "Acima do peso"


print(f"O IMC é {imc:.2f}, e a situação é: {situacao}.")
