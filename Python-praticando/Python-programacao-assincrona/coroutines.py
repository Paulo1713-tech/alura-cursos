import asyncio


async def coroutines(numero):
    print(f"Iniciando tarefa {numero}.")
    await asyncio.sleep(2)
    print(f"Tarefa {numero} concluída!")


async def main():
    await coroutines(1)
    await coroutines(2)


asyncio.run(main())
