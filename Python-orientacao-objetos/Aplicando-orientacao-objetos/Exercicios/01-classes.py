## Exercícios
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

# 1- Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
restaurante_praca = Restaurante()
restaurante_praca.categoria = 'Italiana'

# 2- Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
restaurante_praca.nome = 'Casa Italiana'
nome = restaurante_praca.nome
print(f'Nome do restaurante: {nome}')

#  3-   Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba 
#       uma mensagem informando se o restaurante está ativo ou inativo.
if restaurante_praca.ativo:
    print('O restaurante está ativo.')
else:
    print('O restaurante está inativo.')

# 4-    Acesse o valor do atributo de classe categoria diretamente da classe Restaurante 
#       e armazene em uma variável chamada categoria.
categoria = Restaurante.categoria

# 5- Altere o valor do atributo nome para 'Bistrô'.
restaurante_praca.nome = 'Bistrô'

# 6-    Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' 
#       e categoria 'Fast Food'.
restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

# 7- Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
categoria = restaurante_pizza.categoria
if categoria == 'Fast Food':
    print(restaurante_pizza.categoria)
else:
    print('Não é da categoria Fast Food')

# 8- Mude o estado da instância restaurante_pizza para ativo.
restaurante_pizza.ativo = True

# 9- Imprima no console o nome e a categoria da instância restaurante_praca.
print(f'Nome do Restaurante: {restaurante_pizza.nome} - Categoria: {restaurante_pizza.categoria}')