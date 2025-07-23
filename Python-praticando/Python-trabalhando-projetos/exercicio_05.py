from random import choice, choices, shuffle

MAIUSCULAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MINUSCULAS = "abcdefghijklmnopqrstuvwxyz"
NUMEROS = "0123456789"
ESPECIAIS = "!@#$%&*"

def gerar_senha():
    senha = [
        choice(MAIUSCULAS),
        choice(MINUSCULAS),
        choice(NUMEROS),     
        choice(ESPECIAIS)    
    ]

    todos_caracteres = MAIUSCULAS + MINUSCULAS + NUMEROS + ESPECIAIS
    senha.extend(choices(todos_caracteres, k=8))
    shuffle(senha)
    return ''.join(senha)

print(f"Senha gerada: {gerar_senha()}")