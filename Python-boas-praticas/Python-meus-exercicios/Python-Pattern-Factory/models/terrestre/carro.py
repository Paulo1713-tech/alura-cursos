from models.transporte import Veiculo

class Carro(Veiculo):
    def obter_tipo(self) -> str:
        return "Carro 🚗"

    def obter_quantidade_rodas(self) -> int:
        return 4
