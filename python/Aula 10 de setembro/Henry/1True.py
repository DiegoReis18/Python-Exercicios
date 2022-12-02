#Digitar um valor entre 1 e 10, caso o usuario não siga o pedido, peça novamente
n=int(input("Digite um número entre 1 e 10: "))
while (n<1) or (n>10):
    n=int(input("Siga as instruções corretamente: "))

print("Você digitou",n)


#versão com true
print("\nVersão com true")
while (True):
    n=int(input("Digite um número entre 1 e 10: "))
    if (n>=1) and (n<=10):
        break
    else:
        print("Digite um valor válido")

print("Você digitou",n)
