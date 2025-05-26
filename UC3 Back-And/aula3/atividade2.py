#2.Conte quantos produtos existem por categoria (usar dicionário);################

produtos = [
    {"nome": "Notebook", "categoria": "Eletrônicos"},
    {"nome": "Celular", "categoria": "Eletrônicos"},
    {"nome": "Camisa", "categoria": "Roupas"},
    {"nome": "Calça", "categoria": "Roupas"},
    {"nome": "Geladeira", "categoria": "Eletrodomésticos"},
    {"nome": "TV", "categoria": "Eletrônicos"},
]

categorias = {}

for produto in produtos:
    categoria = produto["categoria"]
    if categoria in categorias:
        categorias[categoria] += 1
    else:
        categorias[categoria] = 1

print(categorias)