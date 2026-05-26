Lista 01 — Questão 07: Progressão e Análise
 Aluno: Lorrayne Isabelle Paz de Oliveira
 Data: 26/05/2026

 ── Sua solução abaixo ──────────────────────────────────────────────────────

print("=== SISTEMA DE ANÁLISE DE NOTAS ===")

notas = []
TOTAL_NOTAS = 10

 1. Coleta e Validação das Notas
POR QUE USAMOS 'WHILE' AQUI? 
 Usamos o 'while' porque não sabemos de antemão quantas vezes o usuário vai digitar 
um valor inválido (letras ou números fora do intervalo). O loop precisa rodar 
indefinidamente ATÉ QUE a lista de notas válidas atinja o tamanho desejado (10).
while len(notas) < TOTAL_NOTAS:
    try:
        entrada = input(f"Digite a nota do {len(notas) + 1}º aluno (0.0 a 10.0): ")
        nota = float(entrada)
        
        # Garante que a nota está no intervalo correto
        if 0.0 <= nota <= 10.0:
            notas.append(nota)
        else:
            print("[ERRO] A nota deve estar estritamente entre 0.0 e 10.0.")
            
    except ValueError:
        print("[ERRO] Entrada inválida! Digite apenas números (use ponto para decimais).")

# 2. Processamento dos Dados
maior_nota = max(notas)
menor_nota = min(notas)
media = sum(notas) / len(notas)

# Contagem de alunos acima da média
# POR QUE USAMOS 'FOR' AQUI?
# Usamos o 'for' porque a coleção de notas já está consolidada e possui um tamanho 
# fixo e conhecido (10 elementos). O 'for' é a estrutura ideal para iterar (percorrer) 
# coleções definidas, passando por cada nota exatamente uma vez.
acima_da_media = 0
for nota in notas:
    if nota > media:
        acima_da_media += 1

# 3. Exibição dos Resultados da Turma
print("\n" + "="*35)
print("       RELATÓRIO DA TURMA        ")
print("="*35)
print(f"Maior nota:             {maior_nota:.1f}")
print(f"Menor nota:             {menor_nota:.1f}")
print(f"Média da turma:         {media:.2f}")
print(f"Alunos acima da média:  {acima_da_media}")
print("-" * 35)

# 4. Classificação Individual dos Alunos
print("Classificação dos Alunos:")
for i, nota in enumerate(notas, start=1):
    if nota >= 7.0:
        status = "Aprovado"
    elif nota >= 5.0:
        status = "Recuperação"
    else:
        status = "Reprovado"
        
    print(f"  Aluno {i:02d}: Nota {nota:4.1f} -> {status}")
print("="*35)


── Justificativa do Uso dos Loops (Resumo em Comentário) ───────────────────
 * Loop WHILE (Coleta de dados): Foi escolhido porque o fluxo depende de uma condição
  que pode falhar repetidamente (validação da nota). O loop garante a insistência 
até que a meta de 10 notas válidas seja cumprida, tratando erros de digitação.

* Loops FOR (Análise e Classificação): Foram escolhidos porque, após a validação, 
  já possuímos uma lista com tamanho exato e estático. O 'for' percorre essa sequência   de forma limpa, direta e otimizada para contar os elementos e exibir o relatório.
