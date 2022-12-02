#Variavel é um espaço reservado na memoria ram

carros=200
espaço=5
motoristas=30
passageiros=60

carrosNOmotoristas=carros-motoristas
carrosYEAHmotoristas=motoristas
Lotação=carrosYEAHmotoristas*espaço

print("Há", carros, "carros disponiveis")

print("Há", motoristas, "motoristas")

print("Há", passageiros, "passageiros")

print("Há", carrosYEAHmotoristas, "carros com motoristas")

print("Há", carrosNOmotoristas, "carros sem motoristas")

print("É possivel transportar", Lotação, "passageiros")
