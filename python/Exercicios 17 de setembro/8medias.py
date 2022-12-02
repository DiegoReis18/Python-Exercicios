#Pedir 8 notas e dizer se foi aprovado

soma=0
for n in range (0,8):
    nota=float(input(f"Digite a nota {n}: "))
    while nota<0 or nota>10:
        nota=float(input("Digite uma nota válida: "))
    else:
        print("inserido")
         
    soma=soma+nota

media=soma/8

if media>=7:
    print("Passou com ",media," de média, parabéns!!")

else:
     print("Reprovado com ",media," de média, mais sorte na próxima")

               
