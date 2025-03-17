from notificacao.notificacao import Notificacao


class NotificacaoEmail(Notificacao):
    def enviar_notificacao(self, cliente, mensagem):
        return print(f'Enviando email para {cliente.nome}: {mensagem}')