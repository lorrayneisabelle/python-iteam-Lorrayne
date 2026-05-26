# ==============================================================================
# DESAFIO 04 — TABUADA PERSONALIZADA
# Aluno: Lorrayne Isabelle Paz de Oliveira
# Data:  26/05/2026
# ==============================================================================

# O loop 'while' permite que o programa continue rodando para várias tabuadas
while True:
    print("\n" + "=" * 30)
    print("    SISTEMA DE TABUADA       ")
    print("=" * 30)
    
    # 1. Solicita o número ao usuário
    entrada = input("Digite um número de 1 a 10 (ou 0 para SAIR): ").strip()
    
    # Validação simples para evitar erros caso o usuário digite letras
    if not entrada.isdigit():
        print("❌ Por favor, digite apenas números inteiros!")
        continue
        
    numero = int(entrada)

    # 3. Garante que o programa pare se o usuário digitar 0
    if numero == 0:
        print("\n👋 Saindo do programa. Até mais!")
        break

    # Validação do intervalo solicitado no enunciado
    if numero < 1 or numero > 10:
        print("⚠️ Número fora do intervalo! Escolha um número entre 1 e 10.")
        continue

    # 2. Utiliza o laço 'for' com 'range' para exibir a tabuada de 1 a 10
    print(f"\n📊 Tabuada do número {numero}:")
    print("-" * 20)
    for i in range(1, 11):
        resultado = numero * i
        print(f"  {numero} x {i:2d} = {resultado}")
    print("-" * 20)
