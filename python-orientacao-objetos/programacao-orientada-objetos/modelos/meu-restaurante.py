class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):        
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}| {self.ativo}'
    
    def __repr__(self):
        return f"Restaurante(nome='{self.nome}', categoria='{self.categoria}', ativo={self.ativo})"
    
    def __eq__(self, other):
        if isinstance(other, Restaurante):
            return self.nome == other.nome and self.categoria == other.categoria
        return False

    def __lt__(self, other):
        if isinstance(other, Restaurante):
            return self.nome < other.nome
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Restaurante):
            return self.nome <= other.nome
        return NotImplemented
    
    def __hash__(self):
        return hash((self.nome, self.categoria))  # Usa tupla para gerar um hash único

    def __format__(self, format_spec):
        if format_spec == "upper":
            return f'{self.nome.upper()} | {self.categoria.upper()}'
        elif format_spec == "lower":
            return f'{self.nome.lower()} | {self.categoria.lower()}'
        else:
            return str(self)
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            # print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')
            print(restaurante)


# Criando objetos
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')
restaurante_pizza_falso = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restaurantes()

# Testando os métodos implementados
print(str(restaurante_pizza))  # __str__
print(repr(restaurante_pizza))  # __repr__
print(restaurante_pizza == restaurante_pizza_falso)  # __eq__

# Testando __dict__
print(restaurante_pizza.__dict__)  # Exibe os atributos do objeto como dicionário

# Testando __class__
print(restaurante_pizza.__class__)  # Mostra a classe do objeto

# Testando __format__
print(format(restaurante_pizza, "upper"))  # Converte para maiúsculas
print(format(restaurante_pizza, "lower"))  # Converte para minúsculas

# Testando __hash__
print(hash(restaurante_pizza))  # Gera um valor hash
print(hash(restaurante_pizza_falso))  # Mesmo hash, pois os valores são iguais

# Testando se podemos usar Restaurante como chave de dicionário
restaurante_dict = {restaurante_pizza: "Famosa pizzaria"}
print(restaurante_dict[restaurante_pizza])  # Deve retornar "Famosa pizzaria"
