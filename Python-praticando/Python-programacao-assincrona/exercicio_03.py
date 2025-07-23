import asyncio, math

resultado = []


async def calculo(numero: int, tempo: int):
    if numero == 0:
        return 1
    await asyncio.sleep(tempo)
    resultado.append((numero, math.factorial(numero)))


async def main():
    numeros = [(5, 3), (3, 1), (7, 3), (4, 2), (6, 3)]
    tasks = [asyncio.create_task(calculo(n, t)) for n, t in numeros]

    await asyncio.gather(*tasks)

    for numero, fatorial in sorted(resultado):
        print(f"Fatorial de {numero} = {fatorial}")


asyncio.run(main())
