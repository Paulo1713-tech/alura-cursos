""""
"Joana está participando de um processo seletivo para uma vaga de desenvolvedora e recebeu um desafio técnico 
de criar uma calculadora para somar, subtrair, multiplicar e dividir dois números.

Sua tarefa é criar um programa usando funções lambda que receba dois números e um operador matemático 
escolhido pelo usuário (+, -, * ou /) e exiba o resultado correspondente.
"""
def calculadora(operador, num, num2):
    operacoes = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y!=0 else 'Error: Divisão por zero'
    }
    if operador not in operacoes:
        return 'Erro: Operação inválida'  # Mensagem para operador desconhecido

    return operacoes.get(operador)(num, num2)

try:
    num = float(input('Digite o primeiro número: '))   
    num2 = float(input('Digite o segundo número: '))   
    operador = str(input('Escolha a operação (| + | - | * | / |): '))

    print(f'O resultado é: {calculadora(operador, num, num2)}')
except ValueError:
    print('Erro: Os valores digitados não são numéricos')