def soma(numero):
    res=10+numero
    return res

me=1  
while me==1:
    n1=float(input("Digite um número: "))
    resultado=soma(n1)
    print("Seu número mais 10 = ",resultado)
    me=int(input("Se quiser repetir, digite 1: "))
else:
    print("fim")

