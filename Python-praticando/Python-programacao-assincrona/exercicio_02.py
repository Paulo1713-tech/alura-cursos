import asyncio


async def tarefa(tarefa: str, tempo: int):
    """
    Corrotina que simula uma tarefa assíncrona.

    Args:
        tarefa (str): Nome da tarefa.
        tempo (int): Duração da tarefa em segundos.
    """
    print(f"Iniciando {tarefa.lower()} ...")
    await asyncio.sleep(tempo)
    print(f"{tarefa} concluída!")


async def main():
    await asyncio.gather(
        tarefa("Download", 5),
        tarefa("Análise de dados", 3),
    )

asyncio.run(main())