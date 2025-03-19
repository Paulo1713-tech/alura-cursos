from models.transporte import Veiculo

class Moto(Veiculo):
    def obter_tipo(self) -> str:
        self.liga_motor()
        return "Moto 🏍️ "

    def obter_quantidade_rodas(self) -> int:
        return 2
    
    def liga_motor(self):
        return print(f'Moto está Ligada!')
    