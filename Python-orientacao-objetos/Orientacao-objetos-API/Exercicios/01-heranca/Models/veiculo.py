class Veiculo:
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._ligado = False

    def __str__(self):
        status = 'ligado' if self._ligado else 'desligado'
        return f'Marca: {self._marca.ljust(25)} | Modelo: {self._modelo.ljust(25)} | Estado: {status}'