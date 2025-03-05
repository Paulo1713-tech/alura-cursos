## Exercícios

# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
pessoas = {
    'pessoa 1': {'nome':'Paulo', 'idade':32, 'cidade':'São Paulo'},
    'pessoa 2': {'nome':'Diandra', 'idade':26, 'cidade':'Caieiras'}
}


# 2 - Utilizando o dicionário criado no item 1:
print(f"\nAntes das alterações: {type(pessoas), pessoas}")

# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
pessoas['pessoa 1']['idade'] = 33
print(f'\n {pessoas['pessoa 1']}')

# Adicione um campo de profissão para essa pessoa;
pessoas['pessoa 1']['profissão'] = 'Analista de Sistemas'
print(f'\n {pessoas['pessoa 1']}')

# Remova um item do dicionário.
del pessoas['pessoa 2']
print(f'\nApós alterações: {pessoas}')

# 3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.
numeros = {1: 1**2, 2: 2**2, 3: 3**2, 4: 4**2, 5: 5**2}
print(f'\nNúmeros e seus quadrados: {numeros}')

# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
chave = input('Digite a chave para verificar: ')
if chave in pessoas['pessoa 1']:
    print(f'A chave "{chave}" existe no dicionário.')
else:
    print(f'A chave "{chave}" não existe no dicionário.')

# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
frase = "o rato roeu a roupa do rei de roma, o rei foi ao brasil"
palavras = frase.split()  # Divide a frase em palavras
frequencia = {}

for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1

print("Frequência das palavras:", frequencia)
