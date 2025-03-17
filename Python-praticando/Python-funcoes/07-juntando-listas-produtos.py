# Digite os produtos separados por vírgula: maçã, banana, pera  
# Digite os preços separados por vírgula: 2.5, 1.2, 3.0 

## Saída esperada:
# maçã: 2.5
# banana: 1.2
# pera: 3.0 

produtos = input('Digite os produtos separados por vírgula: ').split(', ')
precos = list(map(float, input('Digite os preços separados por vírgula: ').split(', ')))

dispensa = dict(zip(produtos, precos))

for produto, preco in dispensa.items():
    print(f'{produto}: {preco}')

