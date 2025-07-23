import asyncio


async def coroutines(numero):
    print(f"Iniciando tarefa {numero}.")
    await asyncio.sleep(3)
    print(f"Tarefa {numero} concluída!")


async def main():
    tarefa1 = asyncio.create_task(coroutines(1))
    tarefa2 = asyncio.create_task(coroutines(2))

    await tarefa1
    await tarefa2


asyncio.run(main())
