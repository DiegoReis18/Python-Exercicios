#Pedir uma idade, mas ela deve ser válida
idade=int(input("Digite sua idade: "))
while idade<0 or idade>150:
    idade=int(input("Não minta para mim ;-; : "))

print("Você tem ",idade," anos")
    
