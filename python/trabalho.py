def primo(num):
    p=1
    for x in range (2,num-1):
        p=num%x
        if p==0:
            return False
    if num==1:
        return False
    else:
        return True

n=int(input("Digite um número de 1 a 100: "))
while n<1 or n>100:
    n=int(input("Digite um número válido entre 1 e 100 por favor!: "))
else:
    verificacao=primo(n)
    if verificacao==True:
        print("O número ",n," é primo")
    elif verificacao==False:
        print("O número ",n," não é primo")
