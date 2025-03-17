from notificacao.notificacao import Notificacao


class NotificacaoSMS(Notificacao):
    def enviar_notificacao(self, cliente, mensagem):
        return print(f'Enviando sms para {cliente.nome}: {mensagem}')