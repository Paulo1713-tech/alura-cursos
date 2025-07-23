import asyncio


cursos = {
    "Python Avançado": {"vagas": 2, "inscritos": []},
    "Java para Iniciantes": {"vagas": 1, "inscritos": []},
    "Machine Learning": {"vagas": 1, "inscritos": []},
}

alunos = [
    {"nome": "Alice", "curso": "Python Avançado"},
    {"nome": "Bruno", "curso": "Python Avançado"},
    {"nome": "Carlos", "curso": "Java para Iniciantes"},
    {"nome": "Daniela", "curso": "Machine Learning"},  # não haverá vaga!
    {"nome": "Alice", "curso": "Python Avançado"},  # Tentativa de inscrição duplicada
    {"nome": "Paulo", "curso": "Python Iniciante"},
]


async def verifica_vaga(curso: str) -> bool:
    """
    Verifica se há vagas disponíveis para um curso específico.
    """
    if curso in cursos and cursos[curso]["vagas"] > 0:
        return True
    return False


async def inscreve_aluno(aluno: dict) -> None:
    await asyncio.sleep(2)
    print(f"\nInscrevendo {aluno['nome']} no curso {aluno['curso']}...")

    if aluno["curso"] not in cursos:
        print(f"Curso {aluno['curso']} não encontrado.")
        return False

    if (await verifica_vaga(aluno["curso"])):
        if aluno["nome"] in cursos[aluno["curso"]]["inscritos"]:
            print(
                f"{aluno['nome']} já está inscrita no curso {aluno['curso']}! Inscrição rejeitada."
            )
            return

        cursos[aluno["curso"]]["vagas"] -= 1
        cursos[aluno["curso"]]["inscritos"].append(aluno["nome"])
        print(f"Inscrição confirmada para {aluno['nome']} no curso {aluno['curso']}!")
    else:
        print(
            f"Turma lotada! {aluno['nome']} não pôde se inscrever no curso {aluno['curso']}."
        )


async def main():
    tasks = [asyncio.create_task(inscreve_aluno(aluno)) for aluno in alunos]
    await asyncio.gather(*tasks)

    print("\nTodas as inscrições foram processadas!")


asyncio.run(main())
