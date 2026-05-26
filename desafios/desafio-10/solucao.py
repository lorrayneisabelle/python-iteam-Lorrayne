# Desafio 10 — Projeto Final — Urna Eletrônica
# Aluno: Lorrayne Isabelle Paz de Oliveira
# Data: 26/05/2026

import os

def limpar_tela():
    """Limpa o console para manter a interface e o voto secretos."""
    os.system('cls' if os.name == 'nt' else 'clear')

# ─── CADASTRO DE CANDIDATOS (Uso de Dicionários) ──────────────────────────────
# Facilita a busca direta pelo número digitado, sem precisar de loops longos.
candidatos = {
    "13": {"nome": "Sarah Connor", "partido": "PST (Partido da Salvação Tecnológica)"},
    "22": {"nome": "Luke Skywalker", "partido": "JOR (Ordem Jedi)"},
    "45": {"nome": "Tony Stark", "partido": "PMI (Partido das Mentes Inovadoras)"}
}

# Inicialização dos contadores de votos
votos_candidatos = {numero: 0 for numero in candidatos}
votos_em_branco = 0
votos_nulos = 0

# Controle de Eleitores (Garante que ninguém vote duas vezes)
eleitores_votantes = set()

# Senha do administrador para encerrar a sessão da urna e apurar os votos
SENHA_ADMIN = "2026admin"

# ─── FLUXO PRINCIPAL DA URNA ──────────────────────────────────────────────────
while True:
    limpar_tela()
    print("=" * 50)
    print("         JUSTIÇA ELEITORAL - URNA ELETRÔNICA      ")
    print("=" * 50)
    print("\n[1] Iniciar Votação")
    print("[2] Encerrar Urna (Apenas Administrador)")
    
    opcao = input("\nEscolha uma opção: ").strip()

    if opcao == "2":
        senha = input("Digite a senha de administrador para encerrar: ")
        if senha == SENHA_ADMIN:
            break
        else:
            print(" Senha incorreta! Operação cancelada.")
            input("\nPressione Enter para continuar...")
            continue

    elif opcao == "1":
        limpar_tela()
        print("-" * 50)
        print("                 IDENTIFICAÇÃO                    ")
        print("-" * 50)
        
        # Validação do Eleitor
        titulo = input("Digite o número do seu Título de Eleitor: ").strip()
        
        if not titulo:
            print(" Título inválido!")
            input("\nPressione Enter para voltar...")
            continue
            
        if titulo in eleitores_votantes:
            print(" ATENÇÃO: Este eleitor já votou!")
            input("\nPressione Enter para voltar...")
            continue

        # Se passou pelas validações, o eleitor está apto
        eleitores_votantes.add(titulo)
        
        # ─── TELA DE VOTO (Anonimato Garantido) ────────────────────────────────
        # A partir daqui, o número do título NÃO está mais associado às próximas variáveis
        limpar_tela()
        print("-" * 50)
        print("                    SEU VOTO                      ")
        print("-" * 50)
        print("Opções válidas:")
        for num, dados in candidatos.items():
            print(f"  [{num}] {dados['nome']} - {dados['partido']}")
        print("  [BRANCO] Para votar em branco")
        print("-" * 50)

        voto = input("Digite o número do candidato ou 'BRANCO': ").strip().upper()

        limpar_tela()
        print("-" * 50)
        print("               CONFIRMAÇÃO DO VOTO                ")
        print("-" * 50)

        if voto == "BRANCO":
            print("Você escolheu: VOTO EM BRANCO")
            tipo_voto = "BRANCO"
        elif voto in candidatos:
            print(f"Candidato: {candidatos[voto]['nome']}")
            print(f"Partido:   {candidatos[voto]['partido']}")
            tipo_voto = voto
        else:
            print("NÚMERO ERRADO/INEXISTENTE")
            print("Você escolheu: VOTO NULO")
            tipo_voto = "NULO"

        print("-" * 50)
        print("CONFIRMA  - Para Gravar este voto")
        print("CORRIGE   - Para Reiniciar este voto")
        print("-" * 50)
        
        confirmacao = input("Deseja confirmar? (S/N): ").strip().upper()

        if confirmacao == "S":
            # Computando o voto anonimamente nos contadores gerais
            if tipo_voto == "BRANCO":
                votos_em_branco += 1
            elif tipo_voto == "NULO":
                votos_nulos += 1
            else:
                votos_candidatos[tipo_voto] += 1
            
            print("\n FIIIIIIIIIP! Voto gravado com sucesso!")
        else:
            # Se ele corrigir/cancelar, removemos o título da lista para que ele possa tentar de novo
            eleitores_votantes.remove(titulo)
            print("\n Voto cancelado. Retornando ao menu...")
            
        input("\nPressione Enter para o próximo eleitor...")

# ─── APURAÇÃO DOS RESULTADOS (Relatório Final) ────────────────────────────────
limpar_tela()
votos_totais = sum(votos_candidatos.values()) + votos_em_branco + votos_nulos

print("=" * 50)
print("              RESULTADO DA APURAÇÃO               ")
print("=" * 50)
print(f"Total de Eleitores que votaram: {len(eleitores_votantes)}")
print(f"Total de Votos Computados:       {votos_totais}")
print("-" * 50)

if votos_totais > 0:
    print("VOTAÇÃO DOS CANDIDATOS:")
    for num, qtd_votos in votos_candidatos.items():
        porcentagem = (qtd_votos / votos_totais) * 100
        print(f" • {candidatos[num]['nome']}: {qtd_votos} voto(s) ({porcentagem:.2f}%)")
    
    pct_branco = (votos_em_branco / votos_totais) * 100
    pct_nulo = (votos_nulos / votos_totais) * 100
    print(f" • Votos em Branco: {votos_em_branco} ({pct_branco:.2f}%)")
    print(f" • Votos Nulos:     {votos_nulos} ({pct_nulo:.2f}%)")
    print("-" * 50)

    # Determinar o Vencedor (Maior número de votos nominais)
    vencedor_num = max(votos_candidatos, key=votos_candidatos.get)
    if votos_candidatos[vencedor_num] > 0:
        print(f" VENCEDOR DA ELEIÇÃO: {candidatos[vencedor_num]['nome']} ({candidatos[vencedor_num]['partido']})")
    else:
        print(" A eleição não teve votos válidos para nenhum candidato.")
else:
    print(" Nenhum voto foi registrado nesta urna.")

print("=" * 50)
print("              URNA ENCERRADA COM SUCESSO          ")
print("=" * 50)
