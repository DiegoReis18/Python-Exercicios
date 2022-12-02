#Criar uma matriz com 5 linhas e 4 colunas, o usuario deve inserir os valores
#Mostrar o maior valor da matriz
#Mostrar a soma de todos valores da matriz
matriz = []
nlinha=int(input("Digite o número de linhas da sua matriz: "))
ncoluna=int(input("Digite o número de linhas da sua matriz: "))

for linha in range(0,nlinha):
    me = []
    for coluna in range (0,ncoluna):
            res=int(input(f"linha{linha} coluna{coluna}: "))
            me.append(res)
    matriz.append(me)

print(matriz)

#Maior
maior=matriz[0][0]
for linha in range (0,nlinha):
    for coluna in range (0,ncoluna):
        if matriz[linha][coluna] > maior:
            maior=matriz[linha][coluna]
       

print("O maior: ",maior)

#Soma
soma=0
for linha in range (0,nlinha):
    for coluna in range (0,ncoluna):
        soma=matriz[linha][coluna]+soma

print("Soma: ",soma)
