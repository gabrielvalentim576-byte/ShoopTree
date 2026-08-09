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
- Consumidor de Notificação

Fluxo da aplicação:

Cadastro de Produto
│
▼
Serviço de Produtos
│
├────────► Serviço de Pagamentos
│
▼
Publicação do evento "produto_criado"
│
▼
EventBus
├────────► Consumidor de Pagamento
└────────► Consumidor de Notificação

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

- o produto é armazenado pelo Serviço de Produtos;
- o Serviço de Produtos realiza a comunicação com o Serviço de Pagamentos;
- o evento `produto_criado` é publicado;
- o EventBus distribui o evento aos consumidores inscritos;
- o consumidor de pagamento recebe o evento;
- o consumidor de notificação recebe o evento;
- a notificação é enviada ao cliente.

---

## Design Pattern Utilizado

### Observer Pattern

O EventBus atua como sujeito (Subject).

Os consumidores de pagamento e notificação atuam como Observers.

Quando um novo produto é criado e o evento `produto_criado` é publicado, todos os observadores registrados para esse evento são notificados automaticamente.

---

## Tecnologias

- Python
- FastAPI
- Uvicorn
- Requests

---

## Como executar

Instale as dependências:

```bash
pip install -r requirements.txt