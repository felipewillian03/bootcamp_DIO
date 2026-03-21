inicial = input("Insira o valor do seu produto:").split()

preco = float(inicial[0])

codigo_promocao = inicial[1].upper()

if codigo_promocao == "S":
    preco_final = preco * 0.90
else:
    preco_final = preco

print(f"Que ótima noticia, o valor final do seu produto é: {preco_final:.2f}R$")