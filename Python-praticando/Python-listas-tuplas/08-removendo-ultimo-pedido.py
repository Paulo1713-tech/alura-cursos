# Paulo está criando uma lista de pedidos para a lanchonete. Ele já tem todos os pedidos, 
# mas percebeu que o último foi inserido por engano e precisa removê-lo.

# Diante deste problema, ajude Paulo criando um programa que automatize essa operação, 
# permitindo listar os pedidos e remover o último item automaticamente.

## Exemplo de Entrada:
# Pedidos feitos (separados por vírgula): Sanduíche, Suco, Sobremesa

# #Saída esperada: 
# Pedidos finais: ['Sanduíche', 'Suco']

pedido = input('Pedidos feitos (separados por vírgula): ').split(', ')
ultimo = (len(pedido)-1)
# sugestão: pedidos.pop()

if ultimo:
    pedido.pop(ultimo)
    print(f'Pedidos finais: {pedido}')