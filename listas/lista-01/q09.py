Lista 01 — Questão 09: EAFP vs LBYL
Aluno:Lorrayne Isabelle Paz de Oliveira
Data: 26/05/2026

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Python
def dividir(a, b):
    """
    Reescrita da função utilizando o estilo EAFP (Easier to Ask for Forgiveness than Permission).
    Tenta executar a operação diretamente e trata a exceção caso ela ocorra.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return None

# Testes rápidos para validação:
print(dividir(10, 2))  # Saída esperada: 5.0
print(dividir(10, 0))  # Saída esperada: None
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. O que significa EAFP?
EAFP é o acrônimo para "Easier to Ask for Forgiveness than Permission" (em tradução livre: "É mais fácil pedir perdão do que permissão").

É uma filosofia de codificação onde você assume que as coisas vão funcionar e simplesmente executa a operação diretamente (try). Se algo der errado no caminho, você captura e trata o erro gerado (except).

Ela se opõe diretamente ao estilo LBYL ("Look Before You Leap" — "Olhe antes de pular"), que era o estilo usado no enunciado original. No LBYL, você usa várias estruturas condicionais (if/else) para testar todas as precondições antes de realizar a operação de fato.

2. Qual versão é mais Pythônica?
A versão EAFP (utilizando try/except) é considerada a mais Pythônica (alinhada com a filosofia e o design da linguagem Python).

Existem três motivos principais para isso:

Desempenho (Cenário Comum): Em Python, o tratamento de exceções é extremamente otimizado. Se o código quase sempre recebe valores válidos (o divisor não é zero na maioria das vezes), o try/except roda mais rápido do que um if que precisa ser testado e avaliado toda santa vez.

Legibilidade: O código foca no "caminho feliz" primeiro. Você lê o que a função deve fazer diretamente no bloco principal e deixa a lógica de tratamento de erros isolada no final do bloco.

Prevenção de Condições de Corrida (Race Conditions): Em sistemas de arquivos ou conexões de rede, o LBYL pode falhar. Por exemplo: se você checar if arquivo_existe:, o arquivo pode ser deletado por outro programa um milissegundo depois do teste e antes de você abri-lo. O EAFP evita isso tentando abrir o arquivo direto e tratando a falha se ela ocorrer.
