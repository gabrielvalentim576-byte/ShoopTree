Contexto
A ShoopTree cresceu sobre uma arquitetura monolítica, o que passou a dificultar escalabilidade, manutenção, implantação e evolução.

Problema arquitetural
Como modernizar a plataforma reduzindo acoplamento, separando responsabilidades e permitindo evolução independente dos serviços?

Alternativas avaliadas

Manter arquitetura monolítica.
Adotar monólito modular.
Adotar microsserviços.
Adotar microsserviços com simulação de comunicação orientada a eventos.

Decisão
Adotar dois microsserviços, Serviço de Produtos e Serviço de Pagamentos, utilizando FastAPI, juntamente com um EventBus simulado para distribuição do evento produto_criado e aplicação do Observer Pattern aos consumidores.

Justificativa técnica
A decisão permite demonstrar separação de responsabilidades, comunicação entre serviços, publicação/consumo de eventos e possibilidade de inclusão de novos consumidores, mantendo a implementação adequada ao escopo de uma prova de conceito.

A comunicação entre o Serviço de Produtos e o Serviço de Pagamentos utiliza HTTP síncrono para demonstrar a integração direta entre os microsserviços.

Após o cadastro do produto, também é publicado o evento `produto_criado` no EventBus. Esse evento é distribuído aos consumidores inscritos, incluindo os consumidores de pagamento e de notificação.

Essa combinação foi adotada na prova de conceito para demonstrar os dois modelos de comunicação e a aplicação do Observer Pattern.

Consequências positivas

separação de responsabilidades;
redução do acoplamento;
possibilidade de evolução dos serviços;
demonstração prática de eventos;
aplicação do Observer.

Consequências negativas

maior complexidade operacional;
necessidade de comunicação entre serviços;
necessidade futura de observabilidade;
EventBus ainda é apenas uma simulação.