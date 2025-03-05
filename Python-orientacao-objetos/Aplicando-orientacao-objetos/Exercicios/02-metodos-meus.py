import pickle

class Restaurante:
    def __init__(self, nome, categoria, ativo=False):        
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {"Ativo" if self.ativo else "Inativo"}'

    def __repr__(self):
        return f"Restaurante(nome='{self.nome}', categoria='{self.categoria}', ativo={self.ativo})"

    def ativar(self):
        """Ativa o restaurante"""
        self.ativo = True

    def desativar(self):
        """Desativa o restaurante"""
        self.ativo = False

    def __reduce__(self):
        """Define como o objeto será serializado com pickle"""
        return (self.__class__, (self.nome, self.categoria, self.ativo))


# Função para salvar lista de restaurantes em um arquivo
def salvar_restaurantes(lista_restaurantes, nome_arquivo="restaurantes.pkl"):
    with open(nome_arquivo, "wb") as arquivo:
        pickle.dump(lista_restaurantes, arquivo)
    print(f"Restaurantes salvos com sucesso em {nome_arquivo}!")


# Função para carregar lista de restaurantes de um arquivo
def carregar_restaurantes(nome_arquivo="restaurantes.pkl"):
    try:
        with open(nome_arquivo, "rb") as arquivo:
            return pickle.load(arquivo)
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado!")
        return []


# Criando alguns restaurantes
restaurante1 = Restaurante("Pizza Express", "Italiana")
restaurante2 = Restaurante("Sushi House", "Japonesa", ativo=True)
restaurante3 = Restaurante("Churrasco Gaúcho", "Brasileira")

# Lista de restaurantes
lista_restaurantes = [restaurante1, restaurante2, restaurante3]

# Salvando os restaurantes
salvar_restaurantes(lista_restaurantes)

# Carregando os restaurantes de volta
restaurantes_carregados = carregar_restaurantes()

# Exibindo os restaurantes carregados
print("\nRestaurantes carregados do arquivo:")
for restaurante in restaurantes_carregados:
    print(restaurante)

# Ativando um restaurante carregado e salvando de novo
if restaurantes_carregados:
    restaurantes_carregados[0].ativar()
    salvar_restaurantes(restaurantes_carregados)

# Carregando novamente para conferir
print("\nApós ativar um restaurante:")
restaurantes_carregados = carregar_restaurantes()
for restaurante in restaurantes_carregados:
    print(restaurante)
