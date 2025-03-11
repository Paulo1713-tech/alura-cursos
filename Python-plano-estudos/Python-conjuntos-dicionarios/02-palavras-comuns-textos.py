# Clara é editora de uma revista e deseja comparar dois artigos para identificar quais palavras aparecem em ambos. 
# Sua tarefa é criar um programa que receba dois textos e exiba o conjunto de palavras comuns entre eles.

## Exemplo de entrada:

# Texto 1: O sol brilha forte no céu azul 
# Texto 2: O céu azul anuncia um dia de sol intenso 

## Saída esperada:

# Palavras em comum: {'o', 'azul', 'sol', 'céu'} 

texto1 = 'O sol brilha forte no céu azul'
texto2 = 'O céu azul anuncia um dia de sol intenso'

conjunto1 = set()
conjunto2 = set()

conjunto1.update(texto1.lower().split())
conjunto2.update(texto2.lower().split())

palavras_comuns = conjunto1.intersection(conjunto2)

print(palavras_comuns)