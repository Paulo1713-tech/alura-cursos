
def palavras_encontradas(texto: str):
    palavras = []
    for _ in texto.split(" "):
        if len(_) > 10:
            palavras.append(_)

    if palavras:
        print(f"Palavras longas encontradas: {', '.join(palavras)}")
    else:
        print(f"Nenhuma palavra longa foi encontrada no texto.")


palavras_encontradas(texto = input("Digite um texto: "))