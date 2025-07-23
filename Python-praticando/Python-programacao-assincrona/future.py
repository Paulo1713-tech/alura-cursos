import asyncio


async def coroutines(futuro: asyncio.Future) -> asyncio.Future:
    """
    Corrotina que aguarda 3 segundos e define o resultado do Future.

    Args:
        futuro (asyncio.Future): Objeto Future que será resolvido.

    Returns:
        asyncio.Future: O mesmo objeto Future, após ser resolvido.
    """
    print("Início.")
    await asyncio.sleep(3)
    return futuro.set_result("Fim.")


async def main():
    """
    Função principal que cria um Future, inicia a corrotina e aguarda o resultado.
    """
    futuro = asyncio.Future()
    asyncio.create_task(coroutines(futuro))
    resultado = await futuro
    print(resultado)


asyncio.run(main())
