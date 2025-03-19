from models.terrestre.carro import Carro
from models.terrestre.moto import Moto
from models.terrestre.caminhao import Caminhao
from models.aereo.aviao import Aviao
from models.maritimo.barco import Barco
from models.transporte import Transporte

class TransporteFactory:
    """Factory para criar diferentes tipos de transporte"""

    @staticmethod
    def criar_transporte(tipo: str, **kwargs) -> Transporte:
        tipos = {
            "carro": Carro(),
            "moto": Moto(),
            "caminhao": Caminhao(),
            "aviao": Aviao(),
            "barco": Barco(kwargs.get("cabines", 500)),
        }
        if tipo.lower() in tipos:
            return tipos[tipo.lower()]
        raise ValueError(f"Tipo de transporte '{tipo}' não suportado!")
