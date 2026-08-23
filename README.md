# ProjetoAgenteAlura
Agente de FAQ — Suporte SaaS

Agente conversacional de atendimento ao cliente que responde dúvidas frequentes de usuários de uma plataforma SaaS, com base em uma base de conhecimento estruturada (FaqSuporteSaas.csv).

Descrição geral

Este projeto implementa um agente de FAQ capaz de entender perguntas em linguagem natural feitas por usuários de um SaaS e retornar respostas precisas, extraídas de uma base de conhecimento curada. O agente cobre temas como login, recuperação de senha, alteração de plano, problemas de pagamento e criação de agentes dentro da plataforma.

O objetivo principal é reduzir o volume de chamados no suporte humano, oferecendo respostas instantâneas e consistentes para as dúvidas mais comuns, e escalar automaticamente para um atendente humano quando a pergunta foge do escopo da base de conhecimento ou exige intervenção manual (ex.: cobrança duplicada, bloqueio de conta).

Fluxo resumido do projeto:
O usuário envia uma pergunta 
A camada de NLU identifica a intenção e as palavras-chave da pergunta.
O motor de busca compara a pergunta com as entradas da base (pergunta, palavras_chave, categoria, subcategoria) e recupera o item mais relevante.
O modelo de linguagem gera a resposta final a partir do campo resposta, adaptando o tom quando necessário.
As regras do campo quando_escalar são avaliadas; se a situação do usuário corresponder a um cenário de escalonamento, o atendimento é transferido para um humano.

Tecnologias e ferramentas utilizadas
Linguagem: Python 3.10+
Busca/recuperação: embeddings de texto (ex.: sentence-transformers) ou busca por palavras-chave (TF-IDF / BM25)
Modelo de linguagem: API de LLM (ex.: Claude, via Anthropic API) para geração e formatação das respostas
Armazenamento da base: arquivo CSV (FaqSuporteSaas.csv), podendo ser migrado para um banco vetorial (ex.: Chroma, FAISS, Pinecone) em produção
Interface de atendimento (opcional): integração via webhook com chat, WhatsApp ou widget web

Exemplos de perguntas que o agente consegue responder
Como faço login?
Esqueci minha senha. O que faço?
Como altero meu plano?
Por que meu pagamento foi recusado?
Como criar um agente?
Como cancelo minha assinatura?
É possível ter mais de um usuário na mesma conta?
Como emito a nota fiscal da minha assinatura?
📝 Exemplos de respostas geradas pelo agente

Pergunta: Como faço login?

Para acessar sua conta, abra a página de login da plataforma e informe o endereço de e-mail cadastrado e sua senha. Depois, selecione o botão "Entrar". Se os dados estiverem corretos, você será direcionado ao painel principal. Caso a senha esteja incorreta, utilize a opção "Esqueci minha senha" para iniciar o processo de recuperação.

Pergunta: Por que meu pagamento foi recusado?

Um pagamento pode ser recusado por motivos como dados incorretos do cartão, cartão expirado, limite insuficiente ou bloqueio do banco emissor. Verifique os dados de pagamento cadastrados e, se possível, tente outro método disponível na plataforma. Se o problema persistir, nossa equipe de suporte pode analisar a transação com mais detalhes.


Pergunta: Já tentei resetar minha senha três vezes e não recebo o e-mail.

Percebi que você já tentou recuperar sua senha sem sucesso. Vou encaminhar seu caso para nossa equipe de suporte, que poderá verificar diretamente o seu cadastro e o envio do e-mail de recuperação. 🔁 Transferindo para atendimento humano...


