# Uma escola está organizando os dados dos alunos para criar um relatório resumido. 
# Cada aluno tem seus dados registrados em uma única entrada, incluindo nome, idade e nota final no semestre. 
# Esses dados devem ser exibidos separadamente para cada aluno no formato abaixo:
"""
Aluno: Nome
Idade: Idade
Nota: Nota

Ajude a escola a desenvolver um programa que registre as informações dos alunos, 
organize os dados e exiba um relatório detalhado com as informações separadamente.

Exemplo de Entrada:
Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula: João, 16, 8.5, Maria, 17, 9.2, Pedro, 15, 7.8

Saída esperada:
Aluno: João
Idade: 16
Nota: 8.5

Aluno: Maria
Idade: 17
Nota: 9.2

Aluno: Pedro
Idade: 15
Nota: 7.8"
"""

dados = input('Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula: ').split(', ')
informacao = []

# Percorre a lista de 3 em 3 (Nome, Idade, Nota)
for i in range(0, len(dados), 3):
    nome = dados[i]
    idade = dados[i + 1]
    nota = dados[i + 2]
    informacao.append((nome, idade, nota))

# Exibe os dados formatados
for aluno in informacao:
    print(f'\nAluno: {aluno[0]}\nIdade: {aluno[1]}\nNota: {aluno[2]}')

## sugestão 
dados = input("Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula: ").split(", ")

for i in range(0, len(dados), 3):
    nome, idade, nota = dados[i], int(dados[i + 1]), float(dados[i + 2])
    print(f"Aluno: {nome}")
    print(f"Idade: {idade}")
    print(f"Nota: {nota}\n")
