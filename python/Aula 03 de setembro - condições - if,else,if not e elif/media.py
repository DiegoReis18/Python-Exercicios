#Calcular o valor da média de 4 notas escolares
#Exibir a situação do aluno

n1=float(input("Digite a sua primeira nota: "))
n2=float(input("Digite a sua segunda nota: "))
n3=float(input("Digite a sua terceira nota: "))
n4=float(input("Digite a sua quarta nota: "))
media=(n1+n2+n3+n4)/4
print("\nSua média foi ",media)

if (media>=7):
    print("Parabens!!! Você foi aprovado sem precisar do exame")
elif (media<7):
    print("Sua media foi menor do que 7, infelizmente você está de exame")
    exame=float(input("\nInsira sua nota no exame: "))
    print("Sua nota no exame foi ",exame)
    if (exame>=5): 
        print("Parabens!!! Você foi aprovado")
    else:
        print("Você foi reprovado ;-;")
else:
    print("ERRO")
