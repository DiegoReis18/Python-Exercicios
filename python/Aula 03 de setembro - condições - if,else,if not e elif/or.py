# OR
#Informa se a pessoa deve trabalhar

num1=int(input("Digite sua idade "))

if (num1<18) or (num1>59):
    print("Você tem ",num1," anos, NÃO deve trabalhar")
else:
    print("Você tem ",num1," anos, precisa arranjar um emprego")

