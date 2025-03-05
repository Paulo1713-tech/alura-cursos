## Exercícios
# 1. Crie uma classe chamada Veiculo com um método abstrato chamado ligar.

# 2. No mesmo arquivo, crie um construtor para a classe Veiculo que aceita os parâmetros marca e modelo.

# 3. Crie uma nova classe chamada Carro que herda da classe Veiculo.

# 4. No construtor da classe Carro, utilize o método super() para chamar o construtor da classe pai e atribua o atributo específico cor à classe filha.

# 5. Em um arquivo chamado main.py, importe a classe Carro.

# 6. No arquivo main.py, instancie três objetos da classe Carro com diferentes características, como marca, modelo e cor.

from Models.carro import Carro

def main():
    carro1 = Carro('Chevrolet', 'Onix LT', 'Prata')
    carro2 = Carro('Fiat', 'Uno', 'Preto')
    carro3 = Carro('Honda', 'Fit', 'Branco')

    print(f"Carro 1: {carro1.marca} {carro1.modelo}, Cor: {carro1.cor}")
    print(f"Carro 2: {carro2.marca} {carro2.modelo}, Cor: {carro2.cor}")
    print(f"Carro 3: {carro3.marca} {carro3.modelo}, Cor: {carro3.cor}")


if __name__ == '__main__':
    main()
