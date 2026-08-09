from eventos.event_bus import EventBus
from eventos.consumer import pagamento_recebido
from eventos.notificacao import enviar_notificacao
from eventos.producer import EventProducer


event_bus = EventBus()

producer = EventProducer(event_bus)

event_bus.subscribe("produto_criado", pagamento_recebido)
event_bus.subscribe("produto_criado", enviar_notificacao)

produto = {
    "nome": "Notebook",
    "preco": 2500
}

producer.publicar("produto_criado", produto)