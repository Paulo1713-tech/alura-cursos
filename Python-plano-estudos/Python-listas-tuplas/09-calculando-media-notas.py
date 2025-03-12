# A professora Helena quer facilitar sua rotina na hora de calcular a média das notas finais da turma. 
# Ela sempre anota as notas dos alunos ao longo do semestre e, no final, precisa de um relatório 
# para saber se a turma está indo bem.

# Para isso, ajude a professora a criar um programa que receba as notas finais de todos os alunos e calcule a média da turma.

## Exemplo de Entrada:
# Digite as notas dos alunos separadas por vírgula: 8.5, 7.0, 9.2, 6.8

## Saída esperada:
# Média final da turma: 7.88

notas = input('Digite as notas dos alunos separadas por vírgula: ').split(', ')
total_notas = (len(notas))
soma = 0

for nota in notas:
    soma += float(nota)

media = round((soma/total_notas), 2)
print(f'Média final da turma: {media}')

# sugestão 
notas = input("Digite as notas dos alunos separadas por vírgula: ").split(", ")
notas = [float(nota) for nota in notas]
media = sum(notas) / len(notas)
print(f"Média final da turma: {media:.2f}")