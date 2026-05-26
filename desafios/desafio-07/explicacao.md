# Explicação — Desafio 07 — Bio-Calculadora

**Aluno:** Lorrayne Isabelle Paz de Oliveira
**Data:** 26/05/2026

## O que meu programa faz

O projeto consiste em um sistema de cálculos matemáticos dividido de forma modular em dois arquivos:
* **`funcoes_mat.py`:** Atua como nossa biblioteca interna de funções. Ele isola a lógica matemática por trás dos cálculos de área, volume e hipotenusa, usando a biblioteca nativa `math` do Python para garantir precisão técnica.
* **`solucao.py`:** É a interface de controle do usuário. Ele roda um loop que exibe o menu, captura os dados inseridos, faz a chamada das funções importadas do outro arquivo e formata a resposta na tela.

## Resposta à Pergunta Obrigatória

> Por que separar as funções em um arquivo diferente do `solucao.py`? O que muda no projeto quando você tem 50 funções em vez de 3?

Separamos as funções em um arquivo diferente para aplicar o princípio de **Modularização** e **Separação de Responsabilidades**. O arquivo `solucao.py` não precisa saber *como* a matemática é calculada, ele só precisa coletar as entradas e exibir os resultados.
Quando o projeto escala de **3 para 50 funções**, manter tudo em um único arquivo torna o código insustentável. As principais mudanças e impactos práticos seriam:
* **Manutenibilidade:** Se houver um bug em uma fórmula, com arquivos separados você sabe exatamente em qual módulo mexer, sem o risco de quebrar o fluxo de menus e interface do usuário.
* **Organização e Legibilidade:** Encontrar uma linha específica de código em um arquivo único com 50 funções se tornaria um "caos de rolagem" com milhares de linhas de texto. 
* **Reaproveitamento de Código:** Se amanhã decidirmos criar um aplicativo web ou uma interface gráfica para a Bio-Calculadora, podemos importar o mesmo `funcoes_mat.py` sem precisar reescrever nenhuma fórmula.
* **Trabalho em Equipe:** Em projetos reais, um desenvolvedor pode ficar focado em otimizar as 50 funções matemáticas no módulo, enquanto outro trabalha na interface do usuário no arquivo principal, sem que um atrapalhe o arquivo do outro.

## Dificuldades encontradas

A principal dificuldade neste desafio não foi a lógica matemática em si, mas sim a **compreensão do fluxo de importação entre arquivos**. No início, foi preciso atenção para garantir que o arquivo `funcoes_mat.py` estivesse no mesmo diretório (pasta) que o `solucao.py`, caso contrário, o Python não conseguiria localizar o módulo e dispararia um erro de `ModuleNotFoundError`.
Outro ponto que exigiu atenção foi a sintaxe ao chamar as funções no arquivo principal. Foi necessário compreender a diferença entre importar o módulo inteiro (`import funcoes_mat` e depois chamar `funcoes_mat.area_circulo()`) ou importar funções específicas (`from funcoes_mat import area_circulo`). Optei por importar o módulo cheio para manter o código do arquivo principal mais explícito e organizado.
Por fim, precisei pesquisar a documentação da biblioteca nativa `math` para utilizar o valor exato de Pi (`math.pi`) e a função `math.hypot()` para o cálculo da hipotenusa, o que deixou o código mais limpo do que aplicar manualmente a raiz quadrada da soma dos quadrados.

_(Opcional: o que foi difícil? O que você pesquisou para resolver?)_
