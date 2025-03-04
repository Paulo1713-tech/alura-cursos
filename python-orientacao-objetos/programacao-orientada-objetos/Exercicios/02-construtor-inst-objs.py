class Musica:
    musicas = []

    def __init__(self, nome, artista, duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)

    def __str__(self):
        return f'Nome: {self.nome} | Artista: {self.artista} | Duração: {self.duracao}'
    
musica = Musica("I'm a Mess", 'Ed Sheeren', 403)

# exemplos prontos:
musica1 = Musica(nome='Under Pressure', artista='Queen & David Bowie', duracao=248)
musica2 = Musica(nome='The Trooper', artista='Iron Maiden', duracao=245)
musica3 = Musica(nome='Hotel California', artista='Eagles', duracao=390)

for musica in Musica.musicas:
    print(musica)