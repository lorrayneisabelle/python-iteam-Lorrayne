# Lista 02 — Questão 06: Módulo de Estatísticas (módulo estatísticas)
# Aluno: Lorrayne Isabelle Paz de Oliveira
# Data: 26/05/2026

# ── Enunciado ───────────────────────────────────────────────────────────────
# q06_estatisticas.py: crie o módulo com as funções:
#   media(dados), mediana(dados), moda(dados), desvio_padrao(dados)
# Todas devem: receber lista de floats, validar que não está vazia
# (lançar ValueError se estiver), retornar resultado arredondado (2 casas).
# Use apenas stdlib (math permitido, não use statistics).
# 
# q06_main.py: importe o módulo e aplique as 4 funções sobre 10 notas
# digitadas pelo usuário.

# ── Sua solução abaixo ─────────────────────────────────────────────────────
from q06_estatisticas import media, mediana, moda, desvio_padrao

def main():
    print(" ── Captura de Notas do Usuário ── ")
    notas = []
    
    # Loop para garantir a entrada correta de exatamente 10 notas
    while len(notas) < 10:
        try:
            entrada = input(f"Digite a nota {len(notas) + 1}/10: ")
            # Substitui vírgula por ponto para aceitar o padrão decimal brasileiro
            nota = float(entrada.replace(",", "."))
            notas.append(nota)
        except ValueError:
            print("Entrada inválida! Por favor, digite um número válido.")
            
    print("\n" + "─" * 40)
    print(f"Notas digitadas: {notas}")
    print("─" * 40)
    
    # Aplicação e exibição das funções do módulo
    try:
        print(f"Média:         {media(notas)}")
        print(f"Mediana:       {mediana(notas)}")
        print(f"Moda:          {moda(notas)}")
        print(f"Desvio Padrão: {desvio_padrao(notas)}")
    except ValueError as e:
        print(f"Erro ao processar estatísticas: {e}")

if __name__ == "__main__":
    main()
