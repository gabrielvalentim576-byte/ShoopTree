from eventos.event_bus import EventBus
from eventos.consumer import pagamento_recebido
from eventos.notificacao import enviar_notificacao


event_bus = EventBus()

event_bus.subscribe("produto_criado", pagamento_recebido)
event_bus.subscribe("produto_criado", enviar_notificacao)

produto = {
    "nome": "Notebook",
    "preco": 2500
}

event_bus.publish("produto_criado", produto)