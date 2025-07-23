import asyncio

"""
Lista de usuários com suas preferências de notificação.
"""
usuarios = [
    {"nome": "João", "status": "normal", "notificacao": True},
    {"nome": "Carla", "status": "normal", "notificacao": False},
    {"nome": "Ana", "status": "VIP", "notificacao": True},
]


async def enviar_notificacoes(usuario: dict):
    """
    Envia uma notificação para o usuário, se as notificações estiverem ativadas.
    """
    if usuario["notificacao"]:
        print(f"Notificação {usuario['status']} para {usuario['nome']} enviada!")
    else:
        print(f"{usuario['nome']} desativou as notificações. Nada foi enviado.")


async def main():
    """
    Função principal para enviar notificações.
    """
    print("Enviando notificações...")

    # os usuários com status VIP devem ser os primeiros a receber a notificação
    usuarios_vip = [usuario for usuario in usuarios if usuario["status"] == "VIP"]
    usuarios_comuns = [usuario for usuario in usuarios if usuario["status"] == "normal"]

    tasks = [asyncio.create_task(enviar_notificacoes(usuario)) for usuario in usuarios_vip + usuarios_comuns]
    await asyncio.gather(*tasks)

    print("Todas as notificações foram processadas!")


asyncio.run(main())
