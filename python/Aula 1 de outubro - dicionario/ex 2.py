#Pedir 2 matriz (12 cada) e depois somar todos os valores em uma matriz só
#lembre-se 2 listas = 1 matriz
#Juntar 2 matrizes
matriz = []
matriz2= []
novo = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
novamatriz = []
nlinha=int(input("Digite o número de linhas da sua matriz: "))
ncoluna=int(input("Digite o número de linhas da sua matriz: "))

for linha in range(0,nlinha):
    me = []
    for coluna in range (0,ncoluna):
            res=int(input(f"linha{linha} coluna{coluna}: "))
            me.append(res)
    matriz.append(me)

print(matriz)

for linha in range(0,nlinha):
    me2 = []
    for coluna in range (0,ncoluna):
            res2=int(input(f"linha{linha} coluna{coluna}: "))
            me2.append(res2)
    matriz2.append(me2)
    

print(matriz2)

for linha in range (0,nlinha):
    me3= []
    for coluna in range (0,ncoluna):
        ress=matriz[linha][coluna]+matriz2[linha][coluna]
        me3.append(ress)
    novamatriz.append(me3)

print("SOMA")
print(novamatriz)

#Juntar 2 matrizes
for linha in range (0,4):
    for coluna in range (0,3):
        if linha==0 or linha==1:
            novo[linha][coluna] = matriz[linha][coluna]
        elif linha==2:
            novo[linha][coluna] = matriz2[0][coluna]
        elif linha==3:
            novo[linha][coluna] = matriz2[1][coluna]
      
                    
print("Resultado:")
print(novo)
            
        


