# Lista 02 — Questão 05: Funções de Alta Ordem
# Aluno: Lorrayne Isabelle Paz de Oliveira
# Data:  26/05/2026
# ── Enunciado ───────────────────────────────────────────────────────────────
# Em q05.py: escreva aplicar(lista, funcao) que retorna uma nova lista com a
# função aplicada a cada elemento. Demonstre com:
#   (a) função que eleva ao quadrado
#   (b) função que retorna True se o número for par
# 
# Em q05_resposta.txt: explique o que significa dizer que funções são
# 'cidadãs de primeira classe' em Python.

# ── Sua solução abaixo ──────────────────────────────────────────────────────
Esta implementação cria a função de alta ordem `aplicar` (que replica o comportamento básico da função embutida `map`) e demonstra as transformações solicitadas.
def aplicar(lista, funcao):
    """
    Função de Alta Ordem (Higher-Order Function).
    Recebe uma lista e uma função, aplicando essa função a cada elemento
    e retornando uma nova lista com os resultados.
    """
    nova_lista = []
    for elemento in lista:
        resultado = funcao(elemento)
        nova_lista.append(resultado)
    return nova_lista


# ── Funções Auxiliares para Demonstração ────────────────────────────────────

def elevar_ao_quadrado(n):
    return n ** 2

def eh_par(n):
    return n % 2 == 0


# ── Código Principal (Demonstração) ─────────────────────────────────────────
if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5]
    print(f"Lista original: {numeros}\n")

    # (a) Demonstração com função que eleva ao quadrado
    resultados_quadrado = aplicar(numeros, elevar_ao_quadrado)
    print(f"(a) Elementos ao quadrado: {resultados_quadrado}")

    # (b) Demonstração com função que retorna True se for par
    resultados_pares = aplicar(numeros, eh_par)
    print(f"(b) Mapeamento de pares (True/False): {resultados_pares}")

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EXPLICAÇÃO: O que significa dizer que funções são 'Cidadãs de Primeira Classe'?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Dizer que em Python as funções são "Cidadãs de Primeira Classe" (First-Class 
Citizens ou First-Class Functions) significa que elas são tratadas pelo sistema
com os mesmos direitos, privilégios e capacidades de qualquer outro objeto ou 
tipo de dado comum da linguagem (como strings, inteiros, listas ou dicionários).

Na prática, isso se traduz em três capacidades fundamentais:

1. Podem ser passadas como argumentos para outras funções:
   Como visto no código 'q05.py', a função 'elevar_ao_quadrado' foi enviada 
   como um parâmetro comum para dentro da função 'aplicar'.

2. Podem ser retornadas por outras funções:
   Uma função pode criar e "devolver" uma outra função como seu resultado.

3. Podem ser atribuídas a variáveis ou armazenadas em estruturas de dados:
   Você pode fazer 'minha_funcao = print' e depois chamar 'minha_funcao("Olá")',
   ou colocar várias funções dentro de uma lista e percorrê-las em um loop.

Conclusão:
Essa característica é o pilar que permite o paradigma de Programação Funcional 
em Python, viabilizando a criação de "Funções de Alta Ordem" (como a nossa 
função 'aplicar', ou as nativas 'map', 'filter' e 'sorted'), que recebem ou 
retornam outras funções.

```
