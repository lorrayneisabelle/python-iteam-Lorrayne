# Lista 02 — Questão 03: Sistema de Inventário
# Aluno: Lorrayne Isabelle Paz de Oliveira
# Data: 26/05/2026

# ── Enunciado ───────────────────────────────────────────────────────────────
# Implemente com lista de dicionários:
#   1. adicionar_produto(inventario, nome, codigo, quantidade, preco)
#   2. buscar_por_codigo(inventario, codigo)  → produto ou None
#   3. listar_abaixo_do_minimo(inventario, minimo)
#   4. valor_total(inventario)  → soma de quantidade × preço
# Use funções para cada operação. Demonstre as 4 no código principal.

def adicionar_produto(inventario, nome, codigo, quantidade, preco):
    """
    Adiciona um novo produto (representado por um dicionário) ao inventário.
    """
    novo_produto = {
        "nome": nome,
        "codigo": codigo,
        "quantidade": quantidade,
        "preco": preco
    }
    inventario.append(novo_produto)
    print(f"Produto '{nome}' adicionado com sucesso!")


def buscar_por_codigo(inventario, codigo):
    """
    Busca um produto no inventário pelo seu código.
    Retorna o dicionário do produto se encontrado, ou None caso contrário.
    """
    for produto in inventario:
        if produto["codigo"] == codigo:
            return produto
    return None


def listar_abaixo_do_minimo(inventario, minimo):
    """
    Retorna uma lista contendo os produtos cuja quantidade está abaixo do mínimo estipulado.
    """
    produtos_alerta = []
    for produto in inventario:
        if produto["quantidade"] < minimo:
            produtos_alerta.append(produto)
    return produtos_alerta


def valor_total(inventario):
    """
    Calcula e retorna o valor total de todo o estoque (quantidade x preço).
    """
    total = 0.0
    for produto in inventario:
        total += produto["quantidade"] * produto["preco"]
    return total


# ── Código Principal (Demonstração) ─────────────────────────────────────────
if __name__ == "__main__":
    # Inicializando o inventário como uma lista vazia
    meu_inventario = []

    print("--- 1. Demonstração: Adicionar Produtos ---")
    adicionar_produto(meu_inventario, "Teclado Mecânico", "A01", 15, 250.00)
    adicionar_produto(meu_inventario, "Mouse Gamer", "B02", 4, 120.00)
    adicionar_produto(meu_inventario, "Monitor 24'", "C03", 2, 850.00)
    adicionar_produto(meu_inventario, "Cabo HDMI", "D04", 50, 25.00)
    print()

    print("--- 2. Demonstração: Buscar por Código ---")
    # Caso 1: Código existente
    busca1 = buscar_por_codigo(meu_inventario, "B02")
    print(f"Busca 'B02': {busca1}")
    
    # Caso 2: Código inexistente
    busca2 = buscar_por_codigo(meu_inventario, "Z99")
    print(f"Busca 'Z99': {busca2}")
    print()

    print("--- 3. Demonstração: Listar Abaixo do Mínimo ---")
    # Alerta para produtos com menos de 5 unidades no estoque
    limite_minimo = 5
    produtos_criticos = listar_abaixo_do_minimo(meu_inventario, limite_minimo)
    print(f"Produtos com quantidade menor que {limite_minimo}:")
    for prod in produtos_criticos:
        print(f" - {prod['nome']} (Estoque: {prod['quantidade']})")
    print()

    print("--- 4. Demonstração: Valor Total do Inventário ---")
    total_estoque = valor_total(meu_inventario)
    print(f"O valor total acumulado no estoque é: R$ {total_estoque:,.2f}")
