from models.transporte import Maritimo


class Barco(Maritimo):
    def __init__(self, cabines: int):
        self._cabines = max(100, cabines)

    @property
    def cabines(self) -> int:
        return self._cabines
    
    @cabines.setter
    def cabines(self, cabines: int):
        self._cabines = cabines

    def obter_tipo(self) -> str:
        return 'Barco 🛥️ '
    
    def obter_quantidade_cabines(self):
        return self._cabines