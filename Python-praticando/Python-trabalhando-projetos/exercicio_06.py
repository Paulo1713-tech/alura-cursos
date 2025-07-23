from random import choice


opcoes = ["pedra", "papel", "tesoura"]


def game(user: str, machine: str) -> int:
    resultados = {
        ("pedra", "tesoura"): 1,
        ("pedra", "papel"): -1,
        ("papel", "pedra"): 1,
        ("papel", "tesoura"): -1,
        ("tesoura", "papel"): 1,
        ("tesoura", "pedra"): -1,
    }

    if user == machine:
        print(f"Computador escolheu: {machine}")
        print("Empate!")
        return 0

    return resultados.get((user, machine), 0)


opcao_user = input("Escolha: pedra, papel ou tesoura? ").lower()
if opcao_user in opcoes:
    opcao_machine = choice(opcoes)

    if game(opcao_user, opcao_machine) > 0:
        print(f"Computador escolheu: {opcao_machine}\nVocê venceu! ")
    else:
        print(f"Computador escolheu: {opcao_machine}\nVocê perdeu! ")
else:
    print("Opção inválida!")
