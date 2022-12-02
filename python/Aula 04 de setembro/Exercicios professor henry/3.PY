#3
#As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia,
#e R$ 1,00 se forem compradas pelo menos 12.

print("-----Bem vindo ao sacolão do Diegoooo <33-----")
print("Cada maçã custa 1,30. Se pedir mais de 1 duzia, o preço cai para 1,30 <3")
q=int(input("Quantas maçãs deseja? "))

if q<12:
    preco= q*1.30
    print("Você comprou ",q," maçãs, você pagará ",preco," reais, reais, perdeu nossa promoção ;-;")
elif q>=12:
    preco= q*1
    print("Você comprou ",q," maçãs, você pagará ",preco," reais, Você recebeu o desconto <3")
else:
    print("ERROOOOO")

    
    
