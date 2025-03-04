## Em uma carreira de desenvolvimento de software, a prática consistente desempenha um papel fundamental na construção 
# de bases sólidas. Pensando nisso, criamos uma lista de atividades (não obrigatórias) focada em prática 
# para melhorar ainda mais sua experiência de aprendizagem.

# Bora praticar então?

# Desafios

# 1. Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. 
# Inicie o atributo ativo como False por padrão.
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False
    
    def __str__(self):
        return f'Titular: {self.titular.ljust(25)} | Saldo: R$ {self.saldo} | Status: {self.ativo}'
    
    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'

    def ativar_conta(self):
        self._ativo = not self._ativo

# 2. Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada 
# com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
    
contaBancaria1 = ContaBancaria('Diandra Baia', 1030.88)
contaBancaria2 = ContaBancaria('Paulo Sousa', -976.23)

print(contaBancaria1)
print(contaBancaria2)

# 3. Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. 
# Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
contaBancaria3 = ContaBancaria('Raphael', 3456.88)
contaBancaria3.ativar_conta()
print(contaBancaria3)

# 4. Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. 
# Utilize propriedades, se necessário.

# 5. Crie uma instância da classe e imprima o valor da propriedade titular.

# 6. Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. 
# Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.

# 7. Crie um método de classe para a conta ClienteBanco.