
# DESAFIO 02 — CALCULADORA DE IMC
# Aluno: Lorrayne Isabelle Paz de Oliveira
# Data:  26/05/2026
# ==============================================================================

# 1. Solicita o nome do usuário
nome = input("Digite o seu nome: ").strip()

# 2. Solicita o peso e a altura convertendo para float
peso = float(input("Digite o seu peso (ex: 75.5): "))
altura = float(input("Digite a sua altura em metros (ex: 1.75): "))

# 3. Calcula o IMC (Peso dividido pela altura ao quadrado)
imc = peso / (altura ** 2)

# 4. Exibe o resultado formatado com 2 casas decimais
print(f"Olá {nome}, seu IMC é {imc:.2f}")
