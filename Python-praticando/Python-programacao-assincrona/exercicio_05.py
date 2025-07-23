import asyncio


"""
Lista de pedidos com suas informações de pagamento e estoque.
"""
pedidos = [
    {"id": 101, "pagamento_aprovado": True, "estoque_disponivel": True},
    {"id": 102, "pagamento_aprovado": True, "estoque_disponivel": False},
    {"id": 103, "pagamento_aprovado": False, "estoque_disponivel": True},
    {"id": 104, "pagamento_aprovado": True, "estoque_disponivel": True},
    {"id": 105, "pagamento_aprovado": False, "estoque_disponivel": False},
]


async def processar_pedido(pedido: dict):
    """
    Processa pedidos, verificando pagamento e estoque.
    """
    print(f'\nProcessando pedido #{pedido["id"]}...')

    if pedido["pagamento_aprovado"]:
        print(f'Pagamento aprovado para pedido #{pedido["id"]}.')

        if pedido["estoque_disponivel"]:
            print(f'Estoque disponível para pedido #{pedido["id"]}.')
            print(f'Pedido #{pedido["id"]} confirmado! Enviado para entrega.')
        else:
            print(f'Estoque indisponível para pedido #{pedido["id"]}.')
    elif not pedido["pagamento_aprovado"]:
        print(f'Pagamento recusado para pedido #{pedido["id"]}. Pedido cancelado.')


async def main():
    try:
        tasks = [asyncio.create_task(processar_pedido(pedido)) for pedido in pedidos]
        await asyncio.gather(*tasks)
        print(f'\n\nTodos os pedidos foram processados!')
    except Exception as e:
        print(f'\nOcorreu um erro ao processar os pedidos: {e}')


asyncio.run(main())