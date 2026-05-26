# ==============================================================================
# DESAFIO 03 — SISTEMA DE MULTAS
# Aluno: Lorrayne Isabelle Paz de Oliveira
# Data: 26/05/2026

# 1. Solicita a velocidade atual do carro (convertendo para float para aceitar decimais)
velocidade = float(input("Digite a velocidade atual do carro (km/h): "))

LIMITE_VELOCIDADE = 80
VALOR_POR_KM = 7.00

# 2. Estrutura Condicional para verificar a multa
if velocidade > LIMITE_VELOCIDADE:
    print(f"Multado! Você excedeu o limite de {LIMITE_VELOCIDADE}km/h.")
    
    # 3. Calcula o valor da multa
    km_acima = velocidade - LIMITE_VELOCIDADE
    multa = km_acima * VALOR_POR_KM
    
    print(f"Valor da multa: R$ {multa:.2f}")
else:
    # 4. Mensagem caso a velocidade esteja dentro do limite
    print("Boa viagem! Dirija com segurança.")
