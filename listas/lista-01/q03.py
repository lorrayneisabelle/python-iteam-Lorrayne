# Lista 01 — Questão 03: Ficha de Cadastro
# Aluno: Lorrayne Isabelle Paz de Oliveira
# Data:  26/05/2026

# ── Sua solução abaixo ──────────────────────────────────────────────────────

print("=== CADASTRO DE USUÁRIO ===")

try:
    # 1. Coleta dos dados
    nome_completo = input("Digite seu nome completo: ").strip()
    cpf = input("Digite seu CPF (apenas números ou com pontos/traços): ").strip()
    
    # O ano de nascimento pode gerar um erro se o usuário digitar letras, por isso o try/except
    ano_nascimento = int(input("Digite seu ano de nascimento (AAAA): "))
    
    altura = float(input("Digite sua altura em metros (ex: 1.75): "))

    # 2. Processamento (Cálculo da idade baseado no ano atual de 2026)
    ANO_ATUAL = 2026
    idade = ANO_ATUAL - ano_nascimento

    # 3. Exibição dos dados formatados com f-string
    print("\n" + "="*30)
    print("      FICHA CADASTRAL      ")
    print("="*30)
    print(f"Nome Completo:     {nome_completo} (Tipo: {type(nome_completo).__name__})")
    print(f"CPF:               {cpf} (Tipo: {type(cpf).__name__})")
    print(f"Ano de Nascimento: {ano_nascimento} (Tipo: {type(ano_nascimento).__name__})")
    print(f"Idade em 2026:     {idade} anos")
    print(f"Altura:            {altura:.2f}m (Tipo: {type(altura).__name__})")
    print("="*30)

except ValueError:
    print("\n[ERRO]: Entrada inválida! O ano de nascimento deve ser um número inteiro e a altura deve usar ponto (ex: 1.75).")

PERGUNTA: Por que usamos 'float' para a altura e não 'int'?

 RESPOSTA: O tipo 'int' serve exclusivamente para números inteiros (sem casas decimais). 
 A altura humana é uma grandeza contínua que exige precisão milimétrica ou centimétrica 
 quando expressa em metros (por exemplo, 1.75 metros). Se utilizássemos 'int', o Python 
 descartaria os valores após a vírgula/ponto, forçando a altura a ser truncada para 
 1 ou 2 metros, o que tornaria o dado incorreto e inútil para um cadastro. O tipo 'float' 
 permite armazenar esses números de ponto flutuante com as casas decimais necessárias.
