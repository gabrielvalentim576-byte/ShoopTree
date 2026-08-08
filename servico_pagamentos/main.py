from fastapi import FastAPI
from eventos.event_bus import EventBus

app = FastAPI()

event_bus = EventBus()

pagamentos = []


def registrar_pagamento(produto):
    pagamento = {
        "cliente": "Gabriel",
        "produto": produto["nome"],
        "valor": produto["preco"],
        "status": "Pago"
    }

    pagamentos.append(pagamento)

    print("\n==============================")
    print("PAGAMENTO GERADO AUTOMATICAMENTE")
    print(pagamento)
    print("==============================\n")


event_bus.subscribe(
    "produto_cadastrado",
    registrar_pagamento
)


@app.get("/pagamentos")
def listar_pagamentos():
    return pagamentos


@app.post("/pagamentos")
def cadastrar_pagamento(pagamento: dict):
    pagamento["status"] = "Pago"

    pagamentos.append(pagamento)

    print("\n==============================")
    print("PAGAMENTO RECEBIDO VIA API")
    print(pagamento)
    print("==============================\n")

    return {
        "mensagem": "Pagamento registrado com sucesso",
        "pagamento": pagamento
    }

