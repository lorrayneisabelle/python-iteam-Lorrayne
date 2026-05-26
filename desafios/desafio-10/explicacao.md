# Explicação — Desafio 10 — Projeto Final — Urna Eletrônica

**Aluno:** Lorrayne Isabelle Paz de Oliveira
**Data:** 26/05/2026

---

## O que meu programa faz

O meu programa simula o funcionamento completo de uma urna eletrônica para votação. Ele é dividido em três etapas principais:

Cadastro de Candidatos: O sistema inicializa e armazena os dados dos candidatos (como nome, número e partido).

Fluxo de Votação: O programa solicita o número do título de eleitor (ou apenas valida se o usuário já votou). Em seguida, abre a tela de votação onde o eleitor digita o número do seu candidato, exibe a foto/nome na tela para confirmação e permite confirmar, votar em branco ou corrigir.

Apuração dos Resultados: Ao encerrar a votação (através de uma senha de administrador), o programa contabiliza os votos nominais, brancos e nulos, exibindo o percentual de cada candidato e declarando o vencedor.

## Resposta à Pergunta Obrigatória

> Responda às três perguntas abaixo (cada uma em um parágrafo):
1. Como a herança ou dicionários facilitaram o cadastro de candidatos na sua solução?
2. Como você garantiu que o voto permanecesse anônimo e seguro?
3. Qual foi o maior obstáculo técnico que você superou e como resolveu?

Como a herança ou dicionários facilitaram o cadastro de candidatos na sua solução? A utilização de dicionários [ou classes com herança, se você usou POO] foi fundamental para associar o número do candidato diretamente às suas informações. Ao definir o número como a chave do dicionário, o programa consegue buscar instantaneamente o nome e o partido do candidato correspondente no momento em que o eleitor digita o voto, sem a necessidade de percorrer listas longas. Isso tornou o código mais limpo, rápido e evitou redundância de dados.

Como você garantiu que o voto permanecesse anônimo e seguro? Para garantir o anonimato e a segurança, o programa separa completamente a identificação do eleitor do registro do voto. O sistema valida se o título de eleitor é elegível e se ele já votou (registrando a presença em uma lista de controle). Contudo, o voto em si é computado de forma genérica em um contador isolado ou em uma lista embaralhada. Assim, é impossível rastrear e descobrir em qual candidato aquele eleitor específico votou, mantendo o sigilo do voto.

Qual foi o maior obstáculo técnico que você superou e como resolveu? O maior obstáculo foi  tratar as entradas de dados do usuário para que o programa não fechasse por erro se alguém digitasse uma letra no lugar de um número. Para resolver isso, implementei estruturas de tratamento de exceções (try-except) e loops de validação (while True). Isso garantiu que, mesmo se o eleitor digitasse um valor inválido ou um número de candidato inexistente, o sistema exibisse uma mensagem de alerta amigável e permitisse corrigir a digitação sem travar a urna.

---

## Dificuldades encontradas
Validação de Nulos e Brancos: No início, foi desafiador criar a lógica para que números digitados incorretamente fossem computados estritamente como votos nulos, garantindo que o fluxo não quebrasse.

Interface e Fluxo: Manter o terminal limpo a cada nova tela de votação (usando comandos para limpar o console) exigiu testes para que o usuário não ficasse confuso com o histórico de votos anteriores na tela.






_(Opcional: o que foi difícil? O que você pesquisou para resolver?)_
