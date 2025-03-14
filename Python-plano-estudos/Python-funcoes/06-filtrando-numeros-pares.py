
numeros = list(map(int, input('Digite os números separados por espaço: ').split()))

pares = list(filter(lambda x: x % 2 == 0, numeros))
pares_formatados = ', '.join(map(str, pares))

print(f'Números pares: {pares_formatados}')