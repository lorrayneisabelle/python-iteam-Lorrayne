
# 1. Começa com uma lista vazia chamada equipe
equipe = []

print("--- Cadastro de Colaboradores (Digite 'sair' para encerrar) ---")

# 2. Inicia o laço while
while True:
    # Pede o nome do colaborador
    nome = input("\nDigite o nome do colaborador: ").strip()
    
    # Verifica se o usuário quer sair
    if nome.lower() == 'sair':
        break
        
    # Pede o cargo do colaborador
    cargo = input("Digite o cargo do colaborador: ").strip()
    
    # Verifica novamente se o usuário quer sair
    if cargo.lower() == 'sair':
        break
    
    # 3. Salva os dados em um dicionário
    colaborador = {
        "nome": nome,
        "cargo": cargo
    }
    
    # Adiciona o dicionário à lista equipe
    equipe.append(colaborador)
    print(f"✔️ {nome} adicionado com sucesso!")

# 4. Ao digitar "sair", o laço quebra e percorre a lista para imprimir o resultado
print("\n" + "="*40)
print("       RELATÓRIO FINAL DA EQUIPE")
print("="*40)

if not equipe:
    print("Nenhum funcionário foi cadastrado.")
else:
    for funcionario in equipe:
        print(f"Funcionário: {funcionario['nome']} | Cargo: {funcionario['cargo']}")

print("="*40)
