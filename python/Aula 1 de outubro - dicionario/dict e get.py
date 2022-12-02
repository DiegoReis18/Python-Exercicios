lista_dicionario = [('Oi','tutupom'),('Como vai','hetero'),('nhai','gay')]

dicionario_lista = dict(lista_dicionario)
print(dicionario_lista)

print(dicionario_lista.get('Oi','ERROR'))
print(dicionario_lista.get('tutupom','ERROR'))
print(dicionario_lista.get('hetero','ERROR'))

if('Oi' in dicionario_lista):
    print("Cadastrado uhu, corresponde a {}".format(dicionario_lista['Oi']))
else:
    print("ERROR")
