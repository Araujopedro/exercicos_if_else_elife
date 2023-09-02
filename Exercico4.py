'''
As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva
 um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.
'''
maca=int(input("quantidade de maçãs compradas:"))

if maca<=5:
    maca2=maca*1.30
    print(f"o valor pelas maçãs é de R$ {maca2:.2f}")
elif maca>=12:
   maca3= maca*1
   print(f"o valor pelas maçãs é de R$ {maca3:.2f}")
else:
     print(f"o valor pelas maçãs é de R$ {maca:.2f}")
