matriz= [['a','b','c','d','e'],['f','g','h','i','j'],['k','l','m','n','o'],
         ['p','q','r','s','t']]

for linha in range(0,4):
    for coluna in range(0,5):
        print("linha= ",linha,"e Coluna= ",coluna,":",matriz[linha][coluna],"\n", end='  ')
    print("\n")
