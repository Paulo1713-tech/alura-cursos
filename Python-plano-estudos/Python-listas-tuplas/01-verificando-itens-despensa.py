# Roberto está organizando sua despensa e quer verificar se determinados 
# itens já estão armazenados antes de adicioná-los à lista de compras.

# Ajude Roberto a criar um programa que pergunte o item desejado e verifique 
# se ele está na lista de itens disponíveis na despensa. Caso o item não esteja na lista, 
# o programa deve informar que ele precisa ser comprado.

## Exemplo de Entrada:
# Digite o item que você quer verificar: açúcar

## Saída esperada:
# O item açúcar precisa ser comprado.

lista_itens = list(['feijão', 'arroz', 'tomate', 'café'])
existe = False
item = input('Digite o item que você quer verificar: ').lower()

for i in lista_itens:
    if i == item:
        print(f'\nO item {item} já está na lista! Lista: {lista_itens}')
        existe = True
        break

if not existe:
    print(f'O item {item} precisa ser comprado.')

## opção 2:

despensa = ['arroz', 'feijão', 'óleo']
item = input("Digite o item que você quer verificar: ")
if item in despensa:
    print(f"O item {item} já está disponível na despensa.")
else:
    print(f"O item {item} precisa ser comprado.")
print(despensa)