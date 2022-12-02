#incompleto
frase=input("Digite uma frase: ")
pv=input("Digite uma palavra da frase digitada: ")
achar=frase.rfind(pv)
new = frase[achar]
pn=input("Digite uma palavra nova: ")
novo = frase.replace(pv,pn)
print(novo)
