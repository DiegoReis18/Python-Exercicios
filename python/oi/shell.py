from sys import *

script, arq_input = argv

def A(f):
    print(f.red())

def retrocede(f):
    f.seek(0)

def imprime(num_linha,f):
    print(num_linha,f.readline())

print("oi")
arq_atual=open(arq_input)
A(arq_atual)
retrocede(arq_atual)
num_linha=1
imprime(num_linha,arq_atual)
num_linha=num_linha+1
imprime(num_linha,arq_atual)
num_linha=num_linha+1
imprime(num_linha,arq_atual)


