#o exercicio da média eu tirei foto
from sys import *

script, entrada = argv

dados=open(entrada,"r")
print(dados.read)
dados.seek(0)
for linha in dados:
 
    valor=linha.split()
    a=len(valor)
    if a>6:
        print("linha =",linha)
        print("valor=",valor)

dados.close()
        

