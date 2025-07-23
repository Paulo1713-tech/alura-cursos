texto = input("Digite um texto: ").lower()
lista = list(texto)
vogais = ["a", "e", "i", "o", "u", "à", "à", "é", "i", "ó", "ú"]

contem = []

for _ in texto:
    if _ in vogais:
        contem.append(_)

print(f"O texto contém {len(contem)} vogais.")

    