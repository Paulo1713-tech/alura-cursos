## Laura e Ana resolveram fazer compras juntas, mas criaram duas listas diferentes. 
## Elas querem um programa que mostre:

# * Quais itens apareceram nas duas listas
# * Quais foram exclusivos de Laura
# * Quais foram exclusivos da Ana

# Escreva um programa que solicite as listas e mostre os resultados dessas comparações.

## Exemplo de entrada:

# Lista de Laura: leite, pão, café, açúcar 
# Lista de Ana: pão, café, biscoito, chocolate 

## Saída esperada:

# Itens em ambas as listas: pão, café 
# Itens exclusivos de Laura: leite, açúcar 
# Itens exclusivos de Ana: biscoito, chocolate

lista_laura = set()
lista_ana = set()

def main():
    lista_laura.update(['leite', 'pão', 'café', 'açúcar'])
    lista_ana.update(['biscoito', 'pão', 'café', 'chocolate'])

    lista_ambas = lista_laura.intersection(lista_ana)
    lista_diff_laura = lista_laura.difference(lista_ana)
    lista_diff_ana = lista_ana.difference(lista_laura)

    print(f'\nItens em ambas as listas: {", ".join(lista_ambas)}')
    print(f'Itens exclusivos de Laura: {", ".join(lista_diff_laura)}')
    print(f'Itens exclusivos de Ana: {", ".join(lista_diff_ana)}')


if __name__ == '__main__':
    main()