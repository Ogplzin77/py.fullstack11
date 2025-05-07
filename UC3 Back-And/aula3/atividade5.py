#######1.Filtre produtos com preço > 1000 usando list comprehension;#######

produtos = {"nome: processador, preço: 500"},
{"nome: placa mae, preço: 1000"}
{"nome: placa de video gtx, preço: 1800"}

produtos_filtrados = [produto for produto in produtos if produto["preço"] > 1000]

print(produtos_filtrados)



