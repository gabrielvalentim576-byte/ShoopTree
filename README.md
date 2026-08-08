# ShoopTree - Modernização Arquitetural

## Descrição

Este projeto foi desenvolvido como prova de conceito para a disciplina de Software Architecture & Design Patterns.

O objetivo é demonstrar a modernização da plataforma ShoopTree, substituindo uma arquitetura monolítica por uma arquitetura baseada em microsserviços e comunicação orientada a eventos.

---

## Arquitetura

O projeto é composto pelos seguintes serviços:

- Serviço de Produtos
- Serviço de Pagamentos
- EventBus (simulação de eventos)

Fluxo da aplicação:

Cadastro de Produto
        │
        ▼
Serviço de Produtos
        │
        ▼
Publicação de Evento
        │
        ▼
EventBus
      ├────────► Pagamento
      └────────► Notificação

---

## Endpoints

### Serviço de Produtos

GET /produtos

Lista todos os produtos cadastrados.

POST /produtos

Cadastra um novo produto.

---

### Serviço de Pagamentos

GET /pagamentos

Lista todos os pagamentos registrados.

POST /pagamentos

Registra um pagamento.

---

## Comunicação Orientada a Eventos

Após o cadastro de um produto:

- o serviço publica o evento;
- o EventBus distribui o evento;
- o consumidor de pagamento recebe o evento;
- o consumidor de notificação recebe o evento.

---

## Design Pattern Utilizado

Observer Pattern

O EventBus atua como sujeito (Subject).

Os consumidores de pagamento e notificação atuam como Observers.

Quando um novo produto é cadastrado, todos os observadores registrados são automaticamente notificados.

---

## Tecnologias

- Python
- FastAPI
- Uvicorn

---

## Como executar

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o Serviço de Produtos:

```bash
uvicorn servico_produtos.main:app --reload --port 8000
```

Execute o Serviço de Pagamentos:

```bash
uvicorn servico_pagamentos.main:app --reload --port 8001
```

Abra:

```
http://127.0.0.1:8000/docs
```

e

```
http://127.0.0.1:8001/docs
```

para testar os serviços.