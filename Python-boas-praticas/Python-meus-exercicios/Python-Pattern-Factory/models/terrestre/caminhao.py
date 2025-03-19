from models.transporte import Veiculo

class Caminhao(Veiculo):
    def obter_tipo(self) -> str:
        return "Caminhão 🚛"

    def obter_quantidade_rodas(self) -> int:
        return 6
