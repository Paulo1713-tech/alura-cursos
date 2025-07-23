import asyncio
import random


jogos = [
    {"id": 1, "times": "Flamengo vs Palmeiras"},
    {"id": 2, "times": "São Paulo vs Corinthians"},
    {"id": 3, "times": "Grêmio vs Internacional"},
]

RESULTADOS = ["Vitória do Time A", "Vitória do Time B", "Empate"]


async def registrar_aposta(jogo: list, aposta: asyncio.Future):
    time = random.randint(0, 8)
    print(
        f"Aposta no jogo {jogo['id']} ({jogo['times']}) registrada! Aguardando resultado..."
    )

    await asyncio.sleep(time)

    resultado = random.choice(
        [f"Vitória do {jogo['times'].split(' vs ')[0]}", f"Vitória do {jogo['times'].split(' vs ')[1]}", "Empate"]
    )
    aposta.set_result(resultado)

    print(f"Aposta no jogo {jogo['id']} definida: {resultado} (após {time}s).")


async def main():
    apostas = [asyncio.Future() for _ in jogos]
    tasks = [
        asyncio.create_task(registrar_aposta(jogos[i], apostas[i]))
        for i in range(len(jogos))
    ]
    
    await asyncio.sleep(0)
    print()

    await asyncio.gather(*tasks)
    print("\nTodos os resultados foram revelados!")


asyncio.run(main())
