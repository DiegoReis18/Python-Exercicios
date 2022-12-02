#trocar os valores das variaveis para deixar na ordem crescente

num1=int(input("Digite um numero: "))
num2=int(input("Digite outro numero: "))
if (num1<num2):
    print("Ordem crescente: ",num1," e ",num2)
else:
    num1,num2 = num2,num1
    print("Ordem crescente: ",num1," e ",num2)
