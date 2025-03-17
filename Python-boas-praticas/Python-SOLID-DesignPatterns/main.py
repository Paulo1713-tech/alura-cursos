from cliente import Cliente
from item import Item
from pedido.pedido_delivery import PedidoDelivery
from pagamento.pagamento_factory import PagamentoFactory
from notificacao.notificacao_facede import NotificacaoFacede
from observador.observador_status import ObservadorStatus


cliente = Cliente(nome='Paulo', endereco='Rua Antonio Gomes Ferreira, 65, São Paulo, SP, 04257-100')
print(f'Cliente: {cliente.nome}, Endereço: {cliente.endereco}')

item_um = Item(nome='Pizza', preco= 30.0)
item_dois = Item(nome='Refrigerante', preco= 5.0)
itens = [item_um, item_dois]

taxa_entrega = 10.0
pedido = PedidoDelivery(cliente=cliente, itens=itens, taxa_entrega=taxa_entrega)

valor_pedido = pedido.calcular_total()
tipo_pagamento = 'pix'
pagamento = PagamentoFactory.create_pagamento(tipo=tipo_pagamento).processar(valor_pedido)

MENSAGEM_PAGO = 'O pagamento foi confirmado!'
MENSAGEM_PREPARANDO = 'O pedido está sendo preparado!'
MENSAGEM_ENVIADO = 'O pedido saiu para a entrega!'

notificacoes = NotificacaoFacede()
observador = ObservadorStatus(notificacoes)
pedido.adicionar_observador(observador)

pedido.status = MENSAGEM_PAGO
pedido.status = MENSAGEM_PREPARANDO
pedido.status = MENSAGEM_ENVIADO