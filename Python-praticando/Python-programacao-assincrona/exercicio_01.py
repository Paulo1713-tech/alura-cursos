import asyncio


async def temporizador(tempo: int):
    """
    Corrotina que simula uma tarefa assíncrona.

    Args:
        tempo (int): Duração da tarefa em segundos.
    """
    print(f"Iniciando temporizador...")
    await asyncio.sleep(tempo)
    print(f"Tempo finalizado após {tempo} segundos!")


async def main():
    """
    Função principal que cria e aguarda múltiplas corrotinas, exibindo barra de progresso geral.
    """
    await temporizador(3)


asyncio.run(main())