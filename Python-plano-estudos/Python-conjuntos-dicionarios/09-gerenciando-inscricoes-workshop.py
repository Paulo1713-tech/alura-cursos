""" 
Laura está organizando um workshop sobre tecnologia e precisa de um programa que permita 
remover participantes que desistiram do evento. O sistema armazena os participantes em um dicionário, 
onde cada chave é o nome e o valor é um conjunto com os dados do participante. 
O programa deve solicitar o nome de um participante e remover esse nome da 
lista de participantes registrados, caso exista.

## Exemplo de entrada:

participantes = { 
    "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"}, 
    "Workshop 2": {"Fernanda", "Gustavo", "Helena"} 
} 

Nome do participante a ser removido: Carla 

# Saída esperada:

Lista atualizada de participantes: 
Workshop 1: {'Alice', 'Bruno', 'Diego'} 
Workshop 2: {'Fernanda', 'Gustavo', 'Helena'}
"""

participantes = { 
    "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"}, 
    "Workshop 2": {"Fernanda", "Gustavo", "Helena"} 
}

nome = input('Nome do participante a ser removido: ')
removido = False

### deprecated ###
# if nome in participantes["Workshop 1"]:
#     participantes["Workshop 1"].discard(nome)
#     print(f'Participante {nome} excluído da lista {participantes["Workshop 1"]} com sucesso')
# elif nome in participantes["Workshop 2"]:
#     participantes["Workshop 2"].discard(nome)
#     print(f'Participante {nome} excluído da lista {participantes["Workshop 2"]} com sucesso')
# else:
#     print('Participante em nenhuma das listas!')
### deprecated ###

for workshop, inscritos in participantes.items():
    if nome in inscritos:
        inscritos.discard(nome)
        removido = True
        print(f'Participante {nome} removido do {workshop} com sucesso!')
        break

if not removido:
    print('Participante não encontrado em nenhum workshop!')

print("\nLista atualizada de participantes:")
for workshop, inscritos in participantes.items():
    print(f"{workshop}: {inscritos}")