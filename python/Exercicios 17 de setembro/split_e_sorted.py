def quebra (coisa):
    p1 = coisa.split(' ')
    return p1

def ordena(coisa):
    return sorted(coisa)

def primeira (coisa):
    primeira=coisa.pop(0)
    print("primeira ",primeira)

def ultima (coisa):
    primeira=coisa.pop(-1)
    print("primeira ",primeira)

p=input("Digite uma frase: ")
frase=quebra(p)
print(frase)
frasenova=len(frase) #frase nova vira uma lista do conteudo de frase
for n in range(0,frasenova):
    print(frase[n])

print(frase)
frase=ordena(p)
print(frase)
