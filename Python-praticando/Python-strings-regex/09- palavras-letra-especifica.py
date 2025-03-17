import re

titulo = input('Digite o título dos livro: ')
letra = input('Digite a letra inicial para pesquisa: ')

resultado = re.findall(rf'\b{letra}[a-zà-ÿ]*', titulo, re.IGNORECASE)

print(resultado)