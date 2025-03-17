# O clube de atletismo Alura Runners organizou uma corrida e divulgou a lista com a classificação final dos participantes. 
# Mas, um erro foi identificado: um dos nomes está incorreto. O organizador precisa de um programa que permita localizar 
# o nome errado e substituí-lo pelo correto.

# Como você escreveria um programa que solicite o nome errado, o nome correto e atualize a 
# lista exibindo a nova classificação ao final?

## Exemplo de Entrada:
# Digite o nome incorreto: Carlos
# Digite o nome correto: João

## Saída esperada:
# O nome Carlos foi substituído por João.

corredores = ['Ana', 'Carlos', 'Pedro']
nome_incorreto = input('Digite o nome incorreto: ')

if nome_incorreto in corredores:
    posicao = corredores.index(nome_incorreto)
    nome_correto = input('Digite o nome correto: ')
    corredores.pop(posicao)
    corredores.insert(posicao, nome_correto)
    print(f'O nome {nome_incorreto} foi substituído por {nome_correto} \nLista atualizada: {corredores}')
else:
    print(f'Nome não encontrado na lista de corredors: {corredores}')