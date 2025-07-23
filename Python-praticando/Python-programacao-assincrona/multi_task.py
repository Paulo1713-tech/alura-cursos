import asyncio


async def coroutines(nome: str, tempo: int):
    """
    Corrotina que simula uma tarefa assíncrona.

    Args:
        nome (str): Nome da tarefa.
        tempo (int): Duração da tarefa em segundos.
    """
    print(f"Tarefa {nome} iniciada.")
    await asyncio.sleep(tempo)
    print(f"Tarefa {nome} concluída.")
    return nome


async def main():
    """
    Função principal que cria e aguarda múltiplas corrotinas, exibindo barra de progresso geral.
    """
    await asyncio.gather(
        coroutines("1",2),
        coroutines("2",3),
        coroutines("3",1),
    )


asyncio.run(main())
