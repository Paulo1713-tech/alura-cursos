## Nathalia é gerente de uma loja virtual e precisa de um sistema que receba os registros de 
# vendas organizados por categoria de produto. Cada categoria contém uma lista de dicionários 
# representando as vendas individuais, com informações sobre o produto, a quantidade vendida e o valor unitário. 
# Sua tarefa é criar um programa que exiba o total de vendas por categoria.

# Exemplo de entrada:
"""
vendas = { 
    "Eletrônicos": [ 
        {
            "produto": "Smartphone", 
            "quantidade": 5, 
            "valor_unitario": 2000
        }, 
        {
            "produto": "Tablet", 
            "quantidade": 3, 
            "valor_unitario": 1500
        } 
    ], 
    "Eletrodomésticos": [ 
        {"produto": "Geladeira", "quantidade": 2, "valor_unitario": 3000}, 
        {"produto": "Micro-ondas", "quantidade": 4, "valor_unitario": 800} 
    ], 
    "Livros": [ 
        {"produto": "Livro A", "quantidade": 10, "valor_unitario": 50}, 
        {"produto": "Livro B", "quantidade": 5, "valor_unitario": 100} 
    ] 
} 

Saída esperada:

Total de vendas por categoria: 
- Eletrônicos: R$ 14500.00 
- Eletrodomésticos: R$ 9200.00 
- Livros: R$ 1000.00"
"""

vendas = { 
    "Eletrônicos": [ 
        {"produto": "Smartphone", "quantidade": 5, "valor_unitario": 2000}, 
        {"produto": "Tablet", "quantidade": 3, "valor_unitario": 1500} 
    ], 
    "Eletrodomésticos": [ 
        {"produto": "Geladeira", "quantidade": 2, "valor_unitario": 3000}, 
        {"produto": "Micro-ondas", "quantidade": 4, "valor_unitario": 800} 
    ], 
    "Livros": [ 
        {"produto": "Livro A", "quantidade": 10, "valor_unitario": 50}, 
        {"produto": "Livro B", "quantidade": 5, "valor_unitario": 100} 
    ] 
}

print(f'Total de vendas por categoria: ')
for categoria, produtos in vendas.items():
    total_vendas = 0

    for produto in produtos:
        total_vendas += (produto["quantidade"] * produto["valor_unitario"])
    print(f'- {categoria}: R$ {total_vendas:.2f}')
    
