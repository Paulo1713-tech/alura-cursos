""""
"Miguel está desenvolvendo um sistema de cupons de desconto e precisa de uma forma para 
aplicar diferentes taxas de desconto sobre os valores das compras.

Diante deste problema, crie uma closure que gere uma função capaz de calcular o preço final com 
um desconto fixo definido pelo usuário.
"""
def criar_desconto(desconto):
    def calcular_preco(valor):
        return valor - (valor * (desconto / 100))
    return calcular_preco


porcentagem = float(input('Digite a porcentagem de desconto: '))
calcular_preco_final = criar_desconto(porcentagem)

valor = float(input('Digite o valor da compra: '))

print(f'Preço final com desconto: {calcular_preco_final(valor)}')