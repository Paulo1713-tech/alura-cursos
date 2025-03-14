"""
Paulo está desenvolvendo um programa para calcular valores acumulados em um sistema financeiro. Ele precisa somar os todos os números inteiros de 1 até n, onde n é um valor escolhido pelo usuário.

Ajude Paulo criando uma função recursiva que receba um número n e retorne a soma de todos os números inteiros de 1 até N.
Exemplo de entrada:
Digite um número: 5

## Saída esperada:
A soma de 1 a 5 é: 15 

"""

def soma_inteiros(n):
    # Se n for 1, retorna 1
    if n == 1:
        return 1
    # Senão, retorna n + a soma dos números de 1 até (n-1)
    else:
        return n + soma_inteiros(n-1)

n = int(input("Digite um número: "))

soma = soma_inteiros(n)

print(f"A soma de 1 a {n} é: {soma}")
