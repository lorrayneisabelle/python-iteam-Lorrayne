Lista 01 — Questão 10: Análise Crítica de Código
Aluno: Lorrayne Isabelle Paz de Oliveira
Data: 26/05/2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

pyPythondef processar_alunos(alunos=None):
    """
    Versão corrigida e pythônica da função.
    Remove o argumento padrão mutável, simplifica a iteração e otimiza a lista.
    """
    # Correção 1: Tratamento correto para argumento padrão omisso
    if alunos is None:
        alunos = []
        
    aprovados = []
    
    # Correção 2: Iteração direta sobre os elementos da lista (Iterable)
    for aluno in alunos:
        # Correção 3: Uso do método .append() para eficiência de memória
        if aluno['nota'] >= 7.0:
            aprovados.append(aluno['nome'])
            
    print(aprovados)
    return aprovados  # Boa prática: retornar o valor gerado

# Teste rápido para validação
dados_teste = [
    {'nome': 'Alice', 'nota': 8.5},
    {'nome': 'Bruno', 'nota': 5.0},
    {'nome': 'Carla', 'nota': 7.0}
]
processar_alunos(dados_teste)  # Saída esperada: ['Alice', 'Carla']
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ARQUIVO: q10_resposta.txtAbaixo estão identificados e explicados os 3 problemas de design e performance presentes no código original:1. O Problema na Definição da Função (alunos=[])O que está errado: Uso de um objeto mutável (list) como argumento padrão da função.Por que é um problema: Em Python, os argumentos padrões são avaliados apenas uma vez, no momento em que a função é definida (compilada), e não a cada vez que ela é chamada. Isso significa que todas as chamadas consecutivas que omitirem o parâmetro alunos vão compartilhar e modificar a mesma lista na memória. Se uma chamada alterar essa lista padrão, a próxima chamada receberá uma lista já "suja", causando bugs de persistência de dados fantasmas de uma execução para outra.2. O Problema em Como o Loop é Escrito (for i in range(len(alunos)):)O que está errado: Padrão de iteração baseado em índices (anti-pattern conhecido como "C-style loop").Por que é um problema: O Python foi desenhado para iterar diretamente sobre coleções (iterables). Usar range(len(...)) força o interpretador a criar um gerador de índices desnecessário e obriga você a acessar os elementos via colchetes (alunos[i]) repetidamente. Isso deixa o código mais poluído, menos legível e consome mais processamento sem necessidade alguma.3. O Problema em Como a Lista é Construída (aprovados = aprovados + [...])O que está errado: Criação de novas listas a cada iteração por meio do operador de concatenação (+).Por que é um problema: Toda vez que o operador + une duas listas, o Python precisa alocar um novo espaço de memória para criar uma terceira lista, copiar todos os elementos da lista antiga, adicionar o novo elemento e atualizar a variável. Em listas grandes, isso gera um custo computacional absurdo de tempo e memória ($O(N^2)$). O correto é usar o método .append(), que modifica a lista original in-place de forma extremamente otimizada ($O(1)$).
