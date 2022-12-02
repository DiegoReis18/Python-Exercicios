#Inserir 5 numeros e soma-los
numeros = []

for n in range(0,5):
    x=int(input("Insira um numero: "))
    numeros.append(x)

print("Números digitados: ",numeros)
soma = 0
for n in range(0,len(numeros)):
    soma=numeros[n]+soma
print("Soma total desses numeros: ",soma)
