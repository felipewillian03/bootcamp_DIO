produtos = input("Digite os produtos separados por virgula ou espaço: ").split()

produtos = [produto.upper().strip(",") for produto in produtos]

contador = {}

for produto in produtos:
    if produto in contador:
        contador[produto] += 1
    else:
        contador[produto] = 1

print(contador)

produto_frequente = produtos[0]
frequencia = contador[produtos[0]]

for produto in produtos:
    if contador[produto] > frequencia:
        frequencia = contador[produto]
        produto_frequente = produto


print(f"Produto mais frequente: {produto_frequente}")
print(f"Número de vezes: {frequencia}")