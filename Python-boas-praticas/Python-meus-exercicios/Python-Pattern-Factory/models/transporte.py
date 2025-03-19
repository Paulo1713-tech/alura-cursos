from abc import ABC, abstractmethod

class Transporte(ABC):
    """Interface para todos os meios de transporte"""

    @abstractmethod
    def obter_tipo(self) -> str:
        pass

class Veiculo(Transporte):
    """Classe base para veículos terrestres"""

    @abstractmethod
    def obter_quantidade_rodas(self) -> int:
        pass

class Aeronave(Transporte):
    """Classe base para aeronaves"""

    @abstractmethod
    def obter_quantidade_motores(self) -> int:
        pass

class Maritimo(Transporte):
    """Classe base para veículos marítimos"""
    @abstractmethod
    def obter_quantidade_cabines(self) -> int:
        pass
