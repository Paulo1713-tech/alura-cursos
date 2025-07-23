
valor_conta = 0.00
porcentagem = 0.00

def total_conta(valor_conta: float, porcentagem: float) -> tuple:
    gorjeta = ((porcentagem / 100) * valor_conta)
    valor_total = (gorjeta + valor_conta)
    
    return (valor_total, gorjeta)

try:
    valor_conta = float(input(f"Digite o valor da conta: "))
    porcentagem = float(input(f"Digite a porcentagem de gorjeta: "))

    pedido = total_conta(valor_conta, porcentagem)

    print(f"\nValor da gorjeta: R$ {pedido[1]}\nTotal a pagar: R$ {pedido[0]}") 
except Exception as e:
    print(f"Ocorreu um erro: {e}")