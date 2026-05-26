# Explicação — Desafio 06 — Bio-Cadastro

**Aluno:** Lorrayne Isabelle Paz de Oliveira
**Data:** 26/06/2026

---

## O que meu programa faz

O programa desenvolvido é um sistema de cadastro de funcionários estruturado em Python. Ele funciona através das seguintes etapas:

Entrada de Dados: O sistema solicita ao usuário que digite as informações essenciais de cada colaborador, como o nome e o cargo.

Estruturação (Dicionários): Cada funcionário inserido é transformado em um dicionário individual, onde as informações são organizadas por chaves ("nome" e "cargo").

Armazenamento (Lista): Esses dicionários são adicionados (append) a uma lista centralizadora, que funciona como o banco de dados temporário do programa.

Saída de Dados: No final, o programa percorre essa lista e exibe na tela os dados de todos os funcionários cadastrados de forma limpa e organizada.

## Resposta à Pergunta Obrigatória

> Por que usamos um **dicionário** para cada funcionário e não uma lista com dois itens como `["Ricardo", "Dev"]`? Qual é a desvantagem de `funcionario[0]` comparado a `funcionario["nome"]`?

Por que usamos um dicionário para cada funcionário e não uma lista com dois itens como ["Ricardo", "Dev"]? Qual é a desvantagem de funcionario[0] comparado a funcionario["nome"]?

Usamos um dicionário porque ele nos permite rotular os dados através de chaves ("nome", "cargo"), tornando o código autoexplicativo (legível).
A principal desvantagem de usar uma lista como funcionario[0] em vez de funcionario["nome"] é a dependência da ordem dos fatores e a falta de clareza:
Legibilidade: Ao ler funcionario["nome"], qualquer programador entende imediatamente que o dado ali é o nome. Ao ler funcionario[0], é impossível adivinhar o que está guardado no índice zero sem ter que procurar onde a lista foi criada.
Manutenção: Se no futuro precisarmos alterar a estrutura e colocar a "Idade" antes do nome, funcionario[0] passaria a quebrar o programa ou a exibir o dado errado. Com o dicionário, a ordem não importa; desde que a chave "nome" exista, o programa continuará funcionando perfeitamente.
## Dificuldades encontradas
O maior desafio inicial foi entender como aninhar (colocar) um dicionário dentro de uma lista e como acessar esses dados depois usando o laço for. Para resolver isso, pesquisei sobre a manipulação de estruturas compostas em Python e fiz alguns testes exibindo o tipo de dado (type()) no console até compreender a lógica de acessar primeiro a posição da lista e, depois, a chave do dicionário.

_(Opcional: o que foi difícil? O que você pesquisou para resolver?)_
