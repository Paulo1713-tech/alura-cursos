# Exemplos:

numero = -1
for _ in range(3):  # Supondo um número máximo de tentativas (3) arbitrário
    numero = int(input("Digite um número positivo: "))
    if numero > 0:
        break

print("Você digitou:", numero)

### ------
#  
numero = -1
while numero <= 0:
    numero = int(input("Digite um número positivo: "))
print("Você digitou:", numero)

### ------
# 
projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]
try:
  for projeto in projetos:
    print(f"Projeto: {projeto}")
except Exception as e:
  print("Ocorreu um erro:", e)

### ------
# 
encomendas = input("Digite os números das encomendas separados por vírgula: ").split(',')
try:
    for encomenda in encomendas:
        print(int(encomenda))
except ValueError:
    print("Uma das entradas não é um número válido.")

### ------
#  1 - Crie uma lista para cada informação a seguir:

# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_nomes = ['Paulo', 'Nicolly', 'Cremilda', 'Cristiane']
lista_ano = ['1992-05-13', '2025-02-11']

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
lista = ['Papel', 'Pedra', 'Tesoura']

for item in lista:
    try:
        print(f'Item da lista: {item} ')
    except ValueError:
        print('Erro encontrado ao listar!')

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
soma = 0
for numero in lista_numeros:
    try:
        if numero % 2 != 0:            
            print(f'\nCálculo: {soma} + {numero}')
            soma = (soma + numero)
            print(f'Soma: {soma}')
    except ValueError:
        print('Erro ao calcular os números!')

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
for i in range(10, 0, -1):
    print(i)

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para 
# imprimir a tabuada desse número, indo de 1 a 10.

numero = int(input('Digite um número: '))
print(f'\nTabuada: {numero}')
      
for n in lista_numeros:
    try:
        print(f'{numero} x {n} = {numero * n}')
    except ValueError:
        print(f'Erro ao calcular tabuada do número: {numero}!')

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. 
# Utilize um bloco try-except para lidar com possíveis exceções.
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

# 7 - Construa um código que calcule a média dos valores em uma lista. 
# Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")