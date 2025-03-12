# Uma ONG está organizando uma campanha de arrecadação de alimentos e precisa registrar
# os nomes dos voluntários que vão ajudar na ação. À medida que os voluntários se inscrevem, 
# seus nomes devem ser adicionados à lista e quando for digitado a palavra sair o programa deve encerrar.

# Ajude a ONG a criar um programa que permita registrar os voluntários e exiba a lista completa no final.

## Exemplo de Entrada:
# Digite o nome do voluntário (ou 'sair' para encerrar): Ana
# Digite o nome do voluntário (ou 'sair' para encerrar): João
# Digite o nome do voluntário (ou 'sair' para encerrar): Mariana
# Digite o nome do voluntário (ou 'sair' para encerrar): sair

## Saída esperada:
# Voluntários registrados: ['Ana', 'João', 'Mariana']
from os import system

def main():
    lista = list([])

    while True:
        system('clear')
        voluntario = input('Digite o nome do voluntário (ou "sair" para encerrar): ').lower()

        if voluntario == 'sair':
            print(f'Voluntários registrados: {lista}')
            break
        
        lista.append(voluntario)

if __name__ == '__main__':
    main()