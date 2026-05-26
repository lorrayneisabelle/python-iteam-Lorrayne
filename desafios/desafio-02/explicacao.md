# Explicação — Desafio 02 — Calculadora de IMC

**Aluno:** Lorrayne Isabelle Paz de Oliveira
**Data:** 26/05/2026

---

## O que meu programa faz

Interage com o usuário: Ele começa exibindo mensagens na tela para pedir três informações básicas: o seu nome, o seu peso (em quilos) e a sua altura (em metros).

Transforma os dados: Como o computador lê o que você digita inicialmente como se fosse apenas um texto (uma palavra), o programa usa o comando float() para transformar o peso e a altura em números decimais reais.

Faz a conta matemática: Com os números prontos, ele aplica a fórmula oficial do IMC.

## Resposta à Pergunta Obrigatória

> Por que é necessário usar `float()` ao capturar peso e altura com `input()`? O que aconteceria se usássemos `int()` para a altura `1.75`?

Por padrão, a função input() no Python captura tudo o que o usuário digita como um texto (do tipo string). Se tentarmos realizar operações matemáticas diretamente com o resultado do input(), o programa gerará um erro, pois o Python não sabe como dividir ou elevar um texto ao quadrado. Por isso, precisamos converter esse texto para um número. Usamos o float() porque o peso e a altura são números decimais (com ponto flutuante), permitindo que o sistema processe valores fracionados como 70.5 ou 1.75.
Se tentássemos usar a função int() para capturar a altura 1.75, o programa interromperia a execução e apresentaria um erro de valor (ValueError). Isso acontece porque a função int() serve estritamente para converter textos que representam números inteiros (como "1", "2", "50"). Ao encontrar o caractere de ponto . na string "1.75", o Python não consegue convertê-lo diretamente em um número inteiro e trava, impedindo o cálculo do IMC.

## Dificuldades encontradas
Formatação das casas decimais: Lembrar da sintaxe correta do :.2f dentro da f-string para arredondar o valor final do IMC sem precisar usar funções externas como round().
Atenção ao separador: No Python, números decimais usam o ponto (.) e não a vírgula (,). Caso o usuário digite a vírgula, o programa também gera um erro, o que me fez entender a importância de futuramente aprender a tratar ou substituir esses caracteres antes da conversão.

_(Opcional: o que foi difícil? O que você pesquisou para resolver?)_
