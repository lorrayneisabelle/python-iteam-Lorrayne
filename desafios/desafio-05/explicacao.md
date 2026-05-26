# Explicação — Desafio 05 — Gerenciador de Compras

**Aluno:** Lorrayne Isabelle Paz de Oliveira
**Data:** 26/05/2026

---

## O que meu programa faz

_(Descreva em suas palavras o que cada parte do código faz.)_

---

## Resposta à Pergunta Obrigatória

Usamos uma lista porque ela é uma estrutura de dados mutável, o que significa que podemos modificar seu conteúdo livremente após ela ter sido criada (adicionando itens, removendo ou alterando a ordem). Como o objetivo do programa é justamente construir um carrinho de compras dinâmico, onde o usuário insere produtos um por um durante a execução do laço while, a lista nos fornece o método .append() para fazer isso de forma direta e eficiente.
Se tentássemos usar uma tupla, o comportamento do programa seria quebrado logo na tentativa de adicionar o primeiro produto. As tuplas são imutáveis — uma vez criadas na memória, seu tamanho e seus elementos não podem ser alterados de forma alguma. Elas não possuem o método .append(). Se tentássemos forçar a adição de um item, o Python geraria um erro de atributo (AttributeError) e travaria o script. Para fazer isso funcionar com tuplas, seríamos obrigados a "recriar" a tupla inteira na memória a cada novo produto digitado (fazendo uma concatenação), o que deixaria o programa lento, confuso e logicamente incorreto para a proposta de um gerenciador.

## Dificuldades encontradas

Tratamento de maiúsculas: No início, se o usuário digitasse "FIM" ou "Fim", o programa continuava rodando. Resolvi isso aplicando o .lower() na verificação da condição de parada.
Ordem Alfabética: Descobri o método .sort() para entregar a lista de compras visualmente organizada ao final, o que deixa o resultado bem mais profissional para quem vai usar no mercado.
_(Opcional: o que foi difícil? O que você pesquisou para resolver?)_
