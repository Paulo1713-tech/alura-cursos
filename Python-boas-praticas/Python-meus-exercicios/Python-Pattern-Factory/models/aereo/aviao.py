from models.transporte import Aeronave

class Aviao(Aeronave):
    def obter_tipo(self) -> str:
        return "Avião ✈️ "

    def obter_quantidade_motores(self) -> int:
        return 2  # Exemplo de um avião comercial pequeno
