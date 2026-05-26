Lista 01 — Questão 06: Validador de Senha
Aluno: Lorrayne Isabelle Paz de Oliveira
Data: 26/05/2026

── Sua solução abaixo ──────────────────────────────────────────────────────

print("=== CADASTRO DE SENHA ===")
tentativas = 0

while True:
    senha = input("\nDigite uma nova senha: ")
    tentativas += 1
    
    # Flags (sinalizadores) para verificar cada critério
    comprimento_ok = len(senha) >= 8
    possui_digito = False
    possui_maiuscula = False
    
    # Varre a string caractere por caractere para validar os critérios 2 e 3
    for caractere in senha:
        if caractere.isdigit():
            possui_digito = True
        if caractere.isupper():
            possui_maiuscula = True
            
    # Se todos os critérios forem atendidos, interrompe o loop
    if comprimento_ok and possui_digito and possui_maiuscula:
        print(f"\n[SUCESSO] Senha válida após {tentativas} tentativa(s).")
        break
    
    # Caso contrário, exibe quais critérios falharam
    print("A senha não atendeu aos seguintes critérios:")
    if not comprimento_ok:
        print("  - Deve ter no mínimo 8 caracteres.")
    if not possui_digito:
        print("  - Deve conter pelo menos um dígito (número).")
    if not possui_maiuscula:
        print("  - Deve conter pelo menos uma letra maiúscula.")
    print("Tente novamente.")
