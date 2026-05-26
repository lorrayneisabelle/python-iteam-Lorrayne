# ==============================================================================
# DESAFIO 05 — GERENCIADOR DE COMPRAS
# Aluno: Lorrayne Isabelle Paz de Oliveira
# Data:  26/06/2026
# ==============================================================================

# 1. Começa com uma lista vazia
lista_compras = []

print("=========================================")
print("      GERENCIADOR DE COMPRAS VIRTUAL     ")
print("=========================================")
print("Digite os produtos que deseja adicionar.")
print("Quando terminar, digite 'fim' para encerrar.")
print("-----------------------------------------")

# 2. Use um laço while para pedir ao usuário nomes de produtos
while True:
    produto = input("Digite o nome do produto: ").strip()
    
    # 4. Pare quando o usuário digitar "fim" (independente de maiúsculas/minúsculas)
    if produto.lower() == "fim":
        break
        
    # Evita que o usuário adicione itens vazios pressionando apenas Enter
    if produto == "":
        print("⚠️ Por favor, digite um nome de produto válido.")
        continue
        
    # 3. Adicione cada produto à lista usando append
    lista_compras.append(produto)
    print(f"✅ '{produto}' adicionado com sucesso!")

# 5. Ao final, exiba a lista organizada e o total de itens com len()
print("\n" + "=" * 40)
print("           SUA LISTA DE COMPRAS          ")
print("=" * 40)

if len(lista_compras) > 0:
    # Ordena a lista em ordem alfabética para exibição organizada
    lista_compras.sort()
    
    for indice, item in enumerate(lista_compras, start=1):
        print(f" {indice}. {item}")
        
    print("-" * 40)
    print(f"🛒 Total de itens na lista: {len(lista_compras)}")
else:
    print("Sua lista está vazia. Nenhum item foi adicionado.")

print("=" * 40)
