X = int(input("Digite um número: "))
Z = int(input("Digite um número: "))	
mmc = 0
if (X > Z):
	mmc = X
else:
	mmc = Z
while (mmc % X != 0 or mmc % Z != 0):
		mmc = mmc + 1
print (mmc)
