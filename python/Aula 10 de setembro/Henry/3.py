#Fazer a divisão de números, se o segundo número for igual a 0, então peça novamente outro número != de 0
n1=float(input("Digite o primeiro valor da divisão: "))
n2=float(input("Digite o segundo valor da divisão: "))
while n2==0:
    n2=float(input("Digite um valor diferente de 0: "))

soma=n1/n2
print(n1," dividido por ",n2," é igual a ",soma)
