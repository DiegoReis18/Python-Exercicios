#elif
#Dizer se o número digitado está situado em quais numeros


x=int(input("Digite um número: "))

if x>=0 and x<=10:
    print("O número ",x," está entre 0 e 10")
elif x>10 and x<=50:
    print("O número ",x," está entre 11 e 50")
elif x>50 and x<=100:
    print("O número ",x," está entre 51 e 100")
else:
    print("O número ",x," é maior que 100")
