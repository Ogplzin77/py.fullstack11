####Remova duplicatas de uma lista de pedidos usando set.#####

pedidos = ['pedido1', 'pedido2', 'pedido1', 'pedido3', 'pedido2', 'pedido4', 'pedido5', 'pedido4', 'pedido5', 'pedido3']

pedidos_sem_duplicatas = list(set(pedidos)) # Usando set para remover duplicatas e converter para uma lista novamente usando list para manter a ordem. 

print(pedidos_sem_duplicatas)
