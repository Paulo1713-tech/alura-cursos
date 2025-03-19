from factory.transporte_factory import TransporteFactory
from models.transporte import Veiculo, Aeronave, Maritimo

if __name__ == "__main__":
    tipos = ["carro", "moto", "caminhao", "aviao", "barco"]

    for tipo in tipos:
        try:
            transporte = TransporteFactory.criar_transporte(tipo)
            if isinstance(transporte, Veiculo):
                print(f"{transporte.obter_tipo()} tem {transporte.obter_quantidade_rodas()} rodas.")
            elif isinstance(transporte, Aeronave):
                print(f"{transporte.obter_tipo()} tem {transporte.obter_quantidade_motores()} motores.")
            elif isinstance(transporte, Maritimo):
                print(f"{transporte.obter_tipo()} - Alterando cabines {transporte.cabines} - tem {transporte.obter_quantidade_cabines()} cabines.")
        except ValueError as e:
            print(e)
