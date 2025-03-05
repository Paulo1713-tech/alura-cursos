# 📌 Prática de Programação em Python

# 📝 Exercícios

# Exercício 1: Criando um Carro
class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

carro1 = Carro("Sedan", "Preto", 2022)
print(carro1.__dict__)

# Exercício 2: Criando um Restaurante
class Restaurante:
    def __init__(self, nome, categoria, capacidade, endereco):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.capacidade = capacidade
        self.endereco = endereco

restaurante1 = Restaurante("Sabor Caseiro", "Brasileira", 100, "Rua das Flores, 123")
print(restaurante1.__dict__)

# Exercício 3: Modificando o Restaurante
class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

restaurante2 = Restaurante("Gourmet Express", "Francesa")
print(restaurante2.__dict__)

# Exercício 4: Melhorando a Exibição
class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    def __str__(self):
        return f"{self.nome} | {self.categoria}"

restaurante3 = Restaurante("Delícias do Mar", "Frutos do Mar")
print(restaurante3)

# Exercício 5: Criando um Cliente
class Cliente:
    def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

cliente1 = Cliente("Ana Souza", 30, "ana@email.com", "(11) 99999-9999")
cliente2 = Cliente("Carlos Lima", 40, "carlos@email.com", "(11) 98888-8888")
cliente3 = Cliente("Mariana Ribeiro", 25, "mariana@email.com", "(11) 97777-7777")

print(cliente1.__dict__)
print(cliente2.__dict__)
print(cliente3.__dict__)
