
def fatorial(num):
    conteudo=1
    for n in range(1,num+1):
        conteudo=conteudo*n
        print(n,"*")
    return conteudo

numero=int(input("Digite um numero: "))
resultado=fatorial(numero)
print("O resultado é igual ",resultado)

    
