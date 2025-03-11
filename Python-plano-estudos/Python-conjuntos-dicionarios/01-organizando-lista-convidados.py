""" 
Ana está organizando uma festa de aniversário e precisa de uma lista de convidados que não tenha repetições , 
pois algumas pessoas foram convidadas mais de uma vez por engano. Ela gostaria que o programa 
solicitasse o nome dos convidados e, ao final, exibisse a lista organizada sem repetições.

Escreva um programa que receba os nomes dos convidados até que o usuário digite 'sair', e ao final 
mostre a lista de convidados sem repetições.

# Exemplo de entrada:

Digite o nome do convidado: Ana 

Digite o nome do convidado: João 

Digite o nome do convidado: Ana 

Digite o nome do convidado: Carla 

Digite o nome do convidado: sair 
Copiar código

# Saída esperada:

Convidados confirmados: Ana, João, Carla
"""
def main():
    convidados = set()

    while True:
        nome = input('Digite o nome do convidado: ').strip().lower()

        if nome.lower() == 'sair':  # Condição de saída
            break
    
        convidados.add(nome)

    print(f'Convidados confirmados: {", ".join(convidados)}')

if __name__ == '__main__':
    main()