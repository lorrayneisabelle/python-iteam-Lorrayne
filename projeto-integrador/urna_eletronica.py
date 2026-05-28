# Projeto Integrador — Urna Eletrônica
# Aluno: Lorrayne Isabelle Paz de Oliveira

# ── Escreva sua solução abaixo ──────────────────────────────────────
--- 1. Criando o Produto ---
Produto: Teclado Mecânico | Preço: R$ 350.00 | Estoque: 10 un
Produto(nome='Teclado Mecânico', preco_inicial=350.0, estoque_inicial=10)

--- 2. Realizando Vendas ---
[VENDA] 4 unidades de 'Teclado Mecânico' vendidas com sucesso.
Produto: Teclado Mecânico | Preço: R$ 350.00 | Estoque: 6 un

--- 3. Realizando Reposição ---
[REPOSIÇÃO] 5 unidades de 'Teclado Mecânico' adicionadas.
Produto: Teclado Mecânico | Preço: R$ 350.00 | Ostoque: 11 un

--- 4. Tentativa de Alterar Preço para Inválido ---
Capturado esperado: O preço do produto deve ser maior que zero.

--- 5. Tentativa de Venda Além do Estoque ---
Capturado esperado: [ERRO DE VENDA] Estoque insuficiente para 'Teclado Mecânico'. Tentou vender: 15, Disponível: 11

--- Estado Final do Produto ---
Produto: Teclado Mecânico | Preço: R$ 350.00 | Estoque: 11 un
