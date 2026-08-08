class EventProducer:

    def __init__(self, event_bus):
        self.event_bus = event_bus

    def publicar(self, nome_evento, dados):
        self.event_bus.publish(nome_evento, dados)