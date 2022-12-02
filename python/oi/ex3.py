#o exercicio da média eu tirei foto
from sys import *

script, entrada = argv

dados=open(entrada,"r")
print(dados.read)
dados.seek(0)
for linha in dados:
 
    valor=linha.split()
    a=len(valor)
    auxiliar=0
    maior=valor[1]
    menor=valor[1]
    for k in range(1,a):
        if valor[k]>maior:
            maior=valor[k]
        elif valor[k]<menor:
            menor=valor[k]
    print("linha =",linha)
    print("valor=",valor)
    print("maior=",maior)
    print("menor=",menor)

dados.close()
        

