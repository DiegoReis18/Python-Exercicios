matriz = []

for linha in range(0,3):
    me = []
    for coluna in range (0,4):
            res=int(input(f"linha{linha} coluna{coluna}: "))
            me.append(res)
    matriz.append(me)

print(matriz)
    
