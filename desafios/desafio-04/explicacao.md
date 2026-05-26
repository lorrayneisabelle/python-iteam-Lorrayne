# Explicação — Desafio 04 — Tabuada Personalizada

**Aluno:** Lorrayne Isabelle Paz de Oliveira
**Data:** 26/06/2026
---

## O que meu programa faz

1. Cria o Menu Principal (while True): Ele abre um ciclo que se repete para sempre. A primeira coisa que ele faz é limpar ou organizar a tela e te perguntar: "Digite um número de 1 a 10 (ou 0 para SAIR)".

2. Valida e Testa o Botão de Saída (if):

Se você digitar 0, o programa lê a condição, exibe uma mensagem de despedida e usa o comando break para quebrar o ciclo e fechar o script.

Se você digitar um número fora do intervalo (como 15 ou uma letra), ele te avisa que está errado e volta para o começo do menu.

3. Calcula a Tabuada (for + range): Se você digitar um número válido (por exemplo, 7), o programa ativa o laço for. Usando o range(1, 11), ele faz uma contagem rápida de 1 até 10. Para cada um desses passos, ele multiplica o seu número e mostra o resultado formatado na tela (ex: 7 x 1 = 7, 7 x 2 = 14...).

4. Reinicia o Ciclo: Assim que o for termina de mostrar a tabuada do 10, o programa não fecha! Como ele está dentro do while, ele volta lá para o topo e te pede outro número.

## Resposta à Pergunta Obrigatória

Para esse exercício, por que for com range() é preferível ao while? Em que cenário o while seria a escolha certa?
O laço for associado à função range() é preferível para exibir a tabuada porque sabemos exatamente a quantidade de vezes que a repetição deve acontecer (exatamente 10 vezes, de 1 a 10). O for torna o código mais limpo, legível e seguro, pois ele mesmo se encarrega de criar a variável de controle, incrementá-la a cada passo e encerrar o loop no momento certo, evitando erros comuns como o esquecimento do incremento.
Por outro lado, o laço while é a escolha certa para cenários onde não sabemos de antemão quantas vezes o código precisará se repetir. O while depende puramente de uma condição ser verdadeira ou falsa para continuar rodando. Um exemplo concreto disso é o próprio menu principal deste desafio (item bônus): não há como prever quantas tabuadas o usuário desejará consultar antes de finalmente digitar 0 para encerrar o programa. O mesmo se aplica a telas de login ou validação de senhas, onde o programa deve repetir o bloco até que a informação correta seja inserida.

## Dificuldades encontradas
Uso combinado dos dois laços: No começo, entender como aninhar um for dentro de um while True pode parecer confuso, mas deu para perceber que o while controla a vida do programa inteiro e o for faz o cálculo rápido da tabuada.
Formatação de alinhamento: Usei o recurso {i:2d} no print para fazer com que os números menores que 10 ocupassem dois espaços na tela, mantendo o sinal de igual (=) perfeitamente alinhado visualmente na tabuada.
_(Opcional: o que foi difícil? O que você pesquisou para resolver?)_
