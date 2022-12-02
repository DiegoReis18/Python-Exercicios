#2
#Ler um valor e escrever se é positivo ou negativo

print("-----RECONHECEDOR DE NÚMEROS-----")
n=float(input("Digite um número: "))

if n > 0:
    print("O número ",n," é POSITIVO (+)")
elif n==0:
    print("O número ",n," é um caso a confuso ")
elif n<0:
    print("O número ",n," é NEGATIVO (-)")
