# Exercícios
import os

## 1 -  Solicite ao usuário que insira um número e, em seguida, 
#       use uma estrutura if else para determinar se o número é par ou ímpar.

os.system('cls')

numero = int(input('Digite um número: '))

if (numero % 2) == 0:
    print(f'{numero} é par!')
else:
    print(f'{numero} é impar!')

## 2 -  Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else 
#       para classificar a idade em categorias de acordo com as seguintes condições:

# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

idade = int(input('\nDigite sua idade: '))

if 0 < idade <= 12:
    print('Criança: 0 a 12 anos')
elif 12 < idade < 18:
     print('Adolescente: 13 a 18 anos')
elif idade >= 18:
     print('Adulto: acima de 18 anos')
else:
     print('Valor inválido')

# 3 -   Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar 
#       se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

usuario_default = 'dbjesus'
senha_default = 'Diandr@'

usuario = str(input('\nLogin: '))
senha = str(input('\nSenha: '))

if (usuario == usuario_default) and (senha == senha_default):
    print(f'Login sucesso! Bem vindo {usuario}')
else:
    print('Senha ou Usuário inválido!')

# 4 -   Solicite ao usuário as coordenadas (x, y) de um ponto qualquer 
#       e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano 
#       o ponto se encontra de acordo com as seguintes condições:

# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.

x = int(input('\nDigite coordenada X: '))
y = int(input('\nDigite coordenada Y: '))

coordenadas = (x, y)

match coordenadas:
    case (x, y) if x > 0 and y > 0:
        print(f'Primeiro Quadrante: {x} x {y}')
    case (x, y) if x < 0 and y > 0:
        print(f'Segundo Quadrante: {x} x {y}')
    case (x, y) if x < 0 and y < 0:
        print(f'Terceiro Quadrante: {x} x {y}')
    case (x, y) if x > 0 and y < 0:
        print(f'Quarto Quadrante: {x} x {y}')
    case _:
        print(f'O ponto está localizado no eixo ou origem.')
