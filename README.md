# ShoopTree - Modernização Arquitetural

## Descrição

Este projeto foi desenvolvido como prova de conceito para a disciplina **Software Architecture & Design Patterns**.

O objetivo é demonstrar a modernização arquitetural da plataforma ShoopTree, originalmente baseada em uma arquitetura monolítica, por meio da separação de responsabilidades em serviços independentes e da utilização de comunicação orientada a eventos.

A solução foi implementada em Python utilizando FastAPI e uma simulação de EventBus em memória para demonstrar publicação, distribuição e consumo de eventos.

---

## Objetivos do Projeto

A prova de conceito busca demonstrar:

* separação de responsabilidades entre serviços;
* implementação de microsserviços independentes;
* comunicação entre serviços por API HTTP;
* comunicação orientada a eventos;
* aplicação do padrão de projeto Observer;
* documentação arquitetural utilizando C4 Model;
* registro de decisão arquitetural por meio de ADR.

---

## Arquitetura

A solução é composta pelos seguintes elementos:

* **Serviço de Produtos**
* **Serviço de Pagamentos**
* **EventBus**
* **Consumidor de Pagamento**
* **Consumidor de Notificação**
* **Gateway de Pagamento** — sistema externo representado na arquitetura
* **Serviço de E-mail / Notificação** — sistema externo representado na arquitetura

### Visão simplificada do fluxo

```text
Cliente
   |
   v
Serviço de Produtos
   |
   +--------------------------> Serviço de Pagamentos
   |                              |
   |                              v
   |                       Gateway de Pagamento
   |
   +----> publica evento "produto_criado"
                 |
                 v
              EventBus
               /    \
              /      \
             v        v
Consumidor de      Consumidor de
Pagamento          Notificação
                      |
                      v
              Serviço de E-mail /
                 Notificação
```

A arquitetura utiliza dois tipos de comunicação:

1. **Comunicação síncrona HTTP**, utilizada entre o Serviço de Produtos e o Serviço de Pagamentos.
2. **Comunicação orientada a eventos simulada**, utilizando o EventBus em memória.

---

## Serviços

### Serviço de Produtos

Responsável pelo cadastro e consulta dos produtos.

**Porta:** `8000`

#### Endpoints

```text
GET /produtos
```

Lista todos os produtos cadastrados.

```text
POST /produtos
```

Cadastra um novo produto.

---

### Serviço de Pagamentos

Responsável pelo registro e gerenciamento dos pagamentos.

**Porta:** `8001`

#### Endpoints

```text
GET /pagamentos
```

Lista todos os pagamentos registrados.

```text
POST /pagamentos
```

Registra um novo pagamento.

---

## Comunicação Orientada a Eventos

Após o cadastro de um produto, o Serviço de Produtos publica o evento:

```text
produto_criado
```

O EventBus recebe esse evento e o distribui aos consumidores inscritos.

O fluxo simulado é:

```text
Produto criado
      |
      v
Publicação do evento "produto_criado"
      |
      v
   EventBus
    /    \
   /      \
  v        v
Pagamento  Notificação
Consumidor Consumidor
             |
             v
          E-mail
```

Dessa forma, diferentes consumidores podem reagir ao mesmo evento sem que o produtor precise conhecer diretamente todos os consumidores.

A implementação utiliza um EventBus em memória, sem dependência de Apache Kafka ou de outro broker externo.

---

## Observer Pattern

### Padrão utilizado

O projeto utiliza o **Observer Pattern**.

O EventBus centraliza a publicação e distribuição dos eventos, enquanto os consumidores representam os observadores interessados nos eventos.

No projeto, os consumidores de pagamento e notificação são registrados no EventBus e recebem o evento `produto_criado` quando ele é publicado.

### Benefícios da utilização

A aplicação do Observer permite:

* reduzir o acoplamento entre produtor e consumidores;
* adicionar novos consumidores sem alterar o produtor;
* distribuir o mesmo evento para diferentes interessados;
* facilitar a evolução da solução.

---

## Tecnologias

* Python
* FastAPI
* Uvicorn
* Requests

---

## Estrutura do Projeto

```text
shoopTree/
│
├── docs/
│   └── ADR-001-modernizacao.md
│
├── eventos/
│
├── servico_pagamentos/
│
├── servico_produtos/
│   ├── __init__.py
│   └── main.py
│
├── .gitignore
├── README.md
├── requirements.txt
└── test_eventos.py
```

---

## Documentação Arquitetural

### C4 Model

O projeto possui dois diagramas arquiteturais:

* **Diagrama de Contexto**
* **Diagrama de Containers**

O Diagrama de Contexto apresenta a ShoopTree, seus usuários e os principais sistemas externos relacionados.

O Diagrama de Containers apresenta os principais serviços e componentes da solução, incluindo o Serviço de Produtos, Serviço de Pagamentos, EventBus e consumidores.

### ADR

A principal decisão arquitetural está registrada em:

```text
docs/ADR-001-modernizacao.md
```

O ADR documenta:

* contexto do problema;
* problema arquitetural;
* alternativas avaliadas;
* decisão tomada;
* justificativa técnica;
* consequências positivas e negativas.

---

## Como Executar

### 1. Criar o ambiente virtual

No Windows PowerShell:

```powershell
python -m venv .venv
```

### 2. Ativar o ambiente virtual

```powershell
.\.venv\Scripts\Activate.ps1
```

Se o ambiente virtual já estiver criado, basta ativá-lo.

---

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

### 4. Executar o Serviço de Produtos

Em um terminal:

```bash
uvicorn servico_produtos.main:app --reload --port 8000
```

O serviço ficará disponível em:

```text
http://127.0.0.1:8000
```

A documentação interativa do FastAPI ficará disponível em:

```text
http://127.0.0.1:8000/docs
```

---

### 5. Executar o Serviço de Pagamentos

Em outro terminal:

```bash
uvicorn servico_pagamentos.main:app --reload --port 8001
```

O serviço ficará disponível em:

```text
http://127.0.0.1:8001
```

A documentação interativa ficará disponível em:

```text
http://127.0.0.1:8001/docs
```

---

## Testando os Serviços

### Produtos

No Swagger do Serviço de Produtos:

```text
http://127.0.0.1:8000/docs
```

É possível executar:

```text
GET /produtos
POST /produtos
```

Exemplo de produto:

```json
{
  "nome": "Notebook",
  "preco": 2500
}
```

### Pagamentos

No Swagger do Serviço de Pagamentos:

```text
http://127.0.0.1:8001/docs
```

É possível executar:

```text
GET /pagamentos
POST /pagamentos
```

---

## Testando a Simulação de Eventos

O projeto possui o arquivo:

```text
test_eventos.py
```

Para executar a simulação:

```bash
python test_eventos.py
```

A execução demonstra a publicação e o consumo de eventos.

Exemplo de saída:

```text
NOVO EVENTO RECEBIDO

Produto: Notebook
Preço: R$ 2500

NOTIFICAÇÃO ENVIADA

O produto 'Notebook' foi comprado com sucesso!
Cliente notificado por e-mail.
```

Essa execução demonstra o funcionamento do EventBus e dos consumidores registrados.

---

## Evidências da Prova de Conceito

Durante os testes foram validados:

* funcionamento do Serviço de Produtos;
* funcionamento do Serviço de Pagamentos;
* cadastro e consulta de produtos;
* registro e consulta de pagamentos;
* publicação de eventos;
* consumo de eventos;
* processamento do consumidor de pagamento;
* envio da notificação;
* execução da aplicação utilizando FastAPI e Uvicorn.

---

## Repositório GitHub

Repositório oficial do projeto:

https://github.com/gabrielvalentim576-byte/ShoopTree

---

## Referências Técnicas

* FastAPI — https://fastapi.tiangolo.com/
* Apache Kafka — https://kafka.apache.org/documentation/
* Structurizr — https://structurizr.com/
* Microservices.io — https://microservices.io/
* C4 Model — https://c4model.com/

---

## Vídeo Pitch

O vídeo de apresentação da solução será disponibilizado após a gravação final.

**Link:** a inserir antes da submissão.

---

