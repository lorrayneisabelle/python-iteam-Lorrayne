# Lista 02 — Questão 08: Herança e Polimorfismo
# Aluno:Lorrayne Isabelle Paz de Oliveira
# Data: 28/05/2026
# ── Enunciado ───────────────────────────────────────────────────────────────
# Implemente:
#   - Funcionario(nome, salario): calcular_bonus() → 10% do salário
#   - Gerente(departamento): bônus = 20%
#   - Estagiario(curso): bônus = 5%
# Crie lista com objetos dos 3 tipos, itere exibindo nome e bônus.
# Explique em comentário: por que o Python chama a versão correta de
# calcular_bonus() sem você verificar o tipo do objeto?

# ── Sua solução abaixo ──────────────────────────────────────────────────────

Python
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self):
        """Retorna o bônus padrão de 10%"""
        return self.salario * 0.10


class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        # Sobrescreve o construtor para adicionar o departamento, mantendo os dados da classe base
        super().__init__(nome, salario)
        self.departamento = departamento

    def calcular_bonus(self):
        """Sobrescreve o método para retornar 20%"""
        return self.salario * 0.20


class Estagiario(Funcionario):
    def __init__(self, nome, salario, curso):
        # Sobrescreve o construtor para adicionar o curso
        super().__init__(nome, salario)
        self.curso = curso

    def calcular_bonus(self):
        """Sobrescreve o método para retornar 5%"""
        return self.salario * 0.05


# ── Execução e Iteração ──────────────────────────────────────────────────────

# Criando a lista com os três tipos de funcionários
funcionarios = [
    Funcionario("Carlos Silva", 5000.00),
    Gerente("Ana Souza", 12000.00, "Tecnologia"),
    Estagiario("Lucas Lima", 1500.00, "Ciência da Computação")
]

print("=== Relatório de Bônus ===")
for f in funcionarios:
    print(f"Nome: {f.nome:<15} | Bônus: R$ {f.calcular_bonus():.2f}")


# ── Explicação Teórica (Resposta do Enunciado) ───────────────────────────────
EXPLICAÇÃO: Por que o Python chama a versão correta de calcular_bonus()?
Esse comportamento ocorre graças a um dos pilares da Programação Orientada a 
Objetos chamado POLIMORFISMO (especificamente, a Sobrescrita de Método ou 
Method Overriding), combinado com o sistema de tipagem dinâmica do Python, 
conhecido como Duck Typing ("se caminha como pato e voa como pato, é um pato").
Em Python, a resolução de métodos acontece em tempo de execução (Dynamic Binding). 
Quando o loop 'for' interage com a lista, a variável 'f' guarda a referência exata 
do objeto na memória. Ao chamarmos 'f.calcular_bonus()', o interpretador do Python 
não olha para o "tipo genérico" da lista, mas sim diretamente para a classe real daquela 
instância específica. 
Se o objeto foi criado como Gerente, o Python busca o método dentro da classe Gerente. 
Se não encontrar lá, ele sobe na hierarquia (MRO - Method Resolution Order) até a 
classe mãe (Funcionario). Como Gerente e Estagiario redefiniram o método, suas próprias 
versões são executadas diretamente, eliminando a necessidade de estruturas condicionais 
manuais (como 'if isinstance(...)').
