from fastapi import FastAPI
import requests

from eventos.event_bus import EventBus
from eventos.consumer import pagamento_recebido
from eventos.notificacao import enviar_notificacao
from eventos.producer import EventProducer

app = FastAPI()

event_bus = EventBus()
producer = EventProducer(event_bus)

event_bus.subscribe(
    "produto_criado",
    pagamento_recebido
)

event_bus.subscribe(
    "produto_criado",
    enviar_notificacao
)

produtos = []


@app.get("/produtos")
def listar_produtos():
    return produtos


@app.post("/produtos")
def cadastrar_produto(produto: dict):
    produtos.append(produto)

    requests.post(
        "http://127.0.0.1:8001/pagamentos",
        json={
            "cliente": "Gabriel",
            "valor": produto["preco"],
            "forma_pagamento": "Cartão de Crédito"
        }
    )

    producer.publicar("produto_criado", produto)

    return {
        "mensagem": "Produto cadastrado com sucesso",
        "produto": produto
    }