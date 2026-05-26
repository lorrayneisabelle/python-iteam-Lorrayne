# Explicação — Desafio 03 — Sistema de Multas

**Aluno:**Lorrayne Isabelle Paz de Oliveira
**Data:** 26/05/2026

---

## O que meu programa faz

1. Captura a Velocidade: O programa começa exibindo uma mensagem na tela perguntando qual é a velocidade atual do carro. Ele usa o comando float() para que você possa digitar números quebrados (como 85.5 km/h), e não apenas números inteiros.

2. Faz o Teste do Limite (A Condicional): O código então analisa o número que você digitou e o compara com o limite de 80 km/h.

3. Caminho A — Se for multado: Caso a velocidade seja maior que 80, o programa entra no bloco do if. Ele calcula quantos quilômetros você passou do limite (Velocidade digitada - 80) e multiplica essa diferença por R$ 7,00. No final, ele te dá um puxão de orelha e mostra o valor exato da multa formatado com duas casas decimais (ex: R$ 35.00).

4. Caminho B — Se estiver tudo bem: Caso a velocidade seja igual ou menor que 80, o programa ignora toda a parte da multa, vai direto para o bloco do else e exibe uma mensagem amigável: "Boa viagem! Dirija com segurança".

## Resposta à Pergunta Obrigatória

Usamos o elif (abreviação de else if) quando queremos criar condições mutuamente exclusivas, ou seja, quando apenas um dos blocos de código deve ser executado. Quando o Python encontra uma condição verdadeira em uma estrutura if / elif / else, ele executa o bloco correspondente e ignora todo o resto. Se usássemos múltiplos if separados, o Python seria obrigado a testar todas as condições uma por uma, mesmo que a primeira já tivesse sido aceita, o que pode fazer com que o programa execute ações duplicadas ou contraditórias.

Exemplo de resultado errado com múltiplos if
Imagine que precisamos criar um sistema que dá um desconto baseado na velocidade de entrega de um serviço (quanto mais rápido, mais pontos). Se usarmos if separados de forma descuidada, um mesmo valor pode ativar dois blocos.

## Dificuldades encontradas
Lógica da Subtração: No início do raciocínio, é preciso atenção para lembrar que a multa não é calculada sobre a velocidade total, mas sim sobre a diferença (velocidade - 80).

Formatação da Moeda: Ajustar a f-string para exibir o valor em Reais com duas casas decimais (R$ {multa:.2f}).
_(Opcional: o que foi difícil? O que você pesquisou para resolver?)_
