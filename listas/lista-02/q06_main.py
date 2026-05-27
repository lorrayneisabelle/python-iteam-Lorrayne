# Lista 02 — Questão 06: Módulo de Estatísticas (programa principal)
# Aluno: Lorrayne Isabelle Paz de Oliveira
# Data: 27/06/2026

# ── Enunciado ───────────────────────────────────────────────────────────────
# q06_estatisticas.py: crie o módulo com as funções:
#   media(dados), mediana(dados), moda(dados), desvio_padrao(dados)
# Todas devem: receber lista de floats, validar que não está vazia
# (lançar ValueError se estiver), retornar resultado arredondado (2 casas).
# Use apenas stdlib (math permitido, não use statistics).
# 
# q06_main.py: importe o módulo e aplique as 4 funções sobre 10 notas
# digitadas pelo usuário.

# ── Sua solução abaixo ──────────────────────────────────────────────────────

import math

def _validar_dados(dados: list[float]) -> None:
    """Valida se a lista existe e não está vazia. Lança ValueError se estiver incorreta."""
    if not dados:
        raise ValueError("A lista de dados não pode estar vazia.")

def media(dados: list[float]) -> float:
    """Calcula a média aritmética simples."""
    _validar_dados(dados)
    resultado = sum(dados) / len(dados)
    return round(resultado, 2)

def mediana(dados: list[float]) -> float:
    """Calcula a mediana dos dados."""
    _validar_dados(dados)
    dados_ordenados = sorted(dados)
    n = len(dados_ordenados)
    meio = n // 2
    
    if n % 2 != 0:
        resultado = dados_ordenados[meio]
    else:
        resultado = (dados_ordenados[meio - 1] + dados_ordenados[meio]) / 2
        
    return round(resultado, 2)

def moda(dados: list[float]) -> float | list[float]:
    """Calcula a moda. Retorna um valor único ou lista em caso de multimodalidade."""
    _validar_dados(dados)
    
    frequencias = {}
    for item in dados:
        frequencias[item] = frequencias.get(item, 0) + 1
        
    max_frequencia = max(frequencias.values())
    modas = [k for k, v in frequencias.items() if v == max_frequencia]
    
    if len(modas) == 1:
        return round(modas[0], 2)
    return [round(m, 2) for m in modas]

def desvio_padrao(dados: list[float]) -> float:
    """Calcula o desvio padrão populacional."""
    _validar_dados(dados)
    
    m = sum(dados) / len(dados)
    soma_quadrados = sum((x - m) ** 2 for x in dados)
    variancia = soma_quadrados / len(dados)
    resultado = math.sqrt(variancia)
    
    return round(resultado, 2)
