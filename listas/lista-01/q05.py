 Lista 01 — Questão 05: Encontre o Bug
Aluno: Lorrayne Isabelle Paz de Oliveira
Data: 26/05/2026

 ── Sua solução abaixo ──────────────────────────────────────────────────────

def maior_nota(notas):
     DICA DE BOA PRÁTICA: Inicializar com 0 funciona para notas (que são positivas),
     mas o ideal para "maior valor" é iniciar com o primeiro elemento: notas[0]
    maior = 0
    for nota in notas:
        if nota > maior:
            maior = nota   CORREÇÃO: Alterado de '==' para '='
    return maior

 Teste do código corrigido
print(f"Maior nota encontrada: {maior_nota([7.5, 9.0, 6.0, 8.5])}")


 Explicação do Bug 
 O erro deste código é um clássico bug de sintaxe/lógica em programação:

1. O que o código original fazia:
   Na linha `maior == nota`, foi utilizado o operador de comparação (==). 
    Isso fazia com que o Python apenas testasse se 'maior' era igual a 'nota', gerando um valor Booleano (True ou False) que era jogado fora logo em seguida.    Como nenhuma atribuição de fato acontecia, a variável 'maior' continuava    sendo 0 até o final da execução.

 2. Como foi corrigido:
  Substituiu-se o operador de comparação (==) pelo operador de atribuição (=). Agora, quando uma nota for maior do que o valor guardado na variável 'maior',   o programa atualiza o valor de 'maior' recebendo essa nova nota.
