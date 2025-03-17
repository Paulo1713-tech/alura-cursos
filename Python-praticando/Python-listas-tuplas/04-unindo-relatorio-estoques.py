# Armano trabalha com a gestão de dois estoques de mercadorias que são representados como tuplas. 
# Agora, ele precisa criar um relatório unificado com os produtos dos dois estoques juntos.

# Para ajudá-lo, como você criaria um programa que ler as informações dos estoques 
# e gera um relatório com todos os produtos juntos?

## Exemplo de Entrada:
# Produtos do estoque 1 (separados por vírgula): Arroz, Feijão, Macarrão
# Produtos do estoque 2 (separados por vírgula): Óleo, Sal, Açúcar

## Saída esperada:
# Estoque combinado:
# ('Arroz', 'Feijão', 'Macarrão', 'Óleo', 'Sal', 'Açúcar')
estoque1 = ('Arroz', 'Feijão', 'Macarrão')
estoque2 = ('Óleo', 'Sal', 'Açúcar')

print(f'Estoque combinado: \n{(estoque1+estoque2)}')
