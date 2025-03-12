# Camila adora receber amigos para jantares temáticos. Para o próximo encontro, 
# ela quer garantir que a ordem de chegada seja respeitada, mas ainda precisa fazer ajustes na lista de convidados. 
# Camila quer adicionar novos nomes e organizá-los em posições específicas.

# Como você criaria um programa que mostre a lista inicial, permita a inserção de um novo nome em uma 
# posição escolhida e exiba a lista atualizada?

## Exemplo de Entrada:
# Lista atual de convidados: ['Ana', 'Pedro', 'Carlos']
# Digite o nome do novo convidado: João
# Digite a posição na qual deseja inserir o convidado: 2

## Saída esperada:
# Lista atualizada de convidados: ['Ana', 'João', 'Pedro', 'Carlos']

lista_inicial = list(['Ana', 'Pedro', 'Carlos'])

print(f'Lista atual de convidados: {lista_inicial}')
novo = input('Digite o nome do novo convidado: ')
posicao = int(input('Digite a posição na qual deseja inserir o convidado: '))

lista_inicial.insert((posicao), novo)
print(f'Lista atualizada de convidados: {lista_inicial}')