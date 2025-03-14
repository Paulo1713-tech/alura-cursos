# Carlos trabalha em um comércio e precisa saber o valor total de vendas realizadas no dia. 
# As vendas são informadas em uma única linha separadas por espaços.

# Sua tarefa é criar um programa que receba essa linha, converta os valores para números e exiba o total.

## Exemplo de entrada:
# Digite os valores das vendas: 100 250 300 

# Saída esperada:
# O total de vendas foi: 650 

def soma_valores(valores):
    total = 0
    for valor in valores.split():
        total += int(valor)
    return total

valores = input('Digite os valores das vendas: ')

total_vendas = soma_valores(valores)

print(f'O total de vendas foi: {total_vendas}')
