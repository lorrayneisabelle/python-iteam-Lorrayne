# Lista 02 — Questão 09: Encapsulamento e Propriedades
# Aluno: Lorrayne Isabelle Paz de Oliveira
# Data: 28/05/2026

# ── Enunciado ───────────────────────────────────────────────────────────────
# Em q09.py — classe Produto com:
#   1. __preco via @property com validação (preço > 0)
#   2. __estoque com getter, repor(qtd) e vender(qtd) — ValueError se sem estoque
#   3. __str__ informativo e __repr__ para debug
# Demonstre: criação, vendas, reposição e tentativa de venda além do estoque.
# 
# Em q09_resposta.txt: explique a diferença entre _atributo e __atributo em Python.

# ── Sua solução abaixo ──────────────────────────────────────────────────────
Parte 1: q09.py (Implementação e Demonstração)
Python
class Produto:
    def __init__(self, nome, preco_inicial, estoque_inicial=0):
        self.nome = nome
        # Utilizamos o setter da propriedade para garantir a validação inicial
        self.preco = preco_inicial
        
        if estoque_inicial < 0:
            raise ValueError("O estoque inicial não pode ser negativo.")
        self.__estoque = estoque_inicial

    # ── Propriedade: Preço (com validação) ──────────────────────────────────
    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco <= 0:
            raise ValueError("O preço do produto deve ser maior que zero.")
        self.__preco = novo_preco

    # ── Getter: Estoque (Apenas leitura via método/propriedade) ─────────────
    @property
    def estoque(self):
        return self.__estoque

    # ── Métodos de Negócio ──────────────────────────────────────────────────
    def repor(self, quantidade):
        if quantidade <= 0:
            raise ValueError("A quantidade de reposição deve ser positiva.")
        self.__estoque += quantidade
        print(f"[REPOSIÇÃO] {quantidade} unidades de '{self.nome}' adicionadas.")

    def vender(self, quantidade):
        if quantidade <= 0:
            raise ValueError("A quantidade de venda deve ser positiva.")
        if quantidade > self.__estoque:
            raise ValueError(
                f"[ERRO DE VENDA] Estoque insuficiente para '{self.nome}'. "
                f"Tentou vender: {quantidade}, Disponível: {self.__estoque}"
            )
        self.__estoque -= quantidade
        print(f"[VENDA] {quantidade} unidades de '{self.nome}' vendidas com sucesso.")

    # ── Representações textuais ─────────────────────────────────────────────
    def __str__(self):
        return f"Produto: {self.nome} | Preço: R$ {self.preco:.2f} | Estoque: {self.__estoque} un"

    def __repr__(self):
        return f"Produto(nome='{self.nome}', preco_inicial={self.preco}, estoque_inicial={self.__estoque})"


# ── Demonstração do Fluxo ───────────────────────────────────────────────────
if __name__ == "__main__":
    print("--- 1. Criando o Produto ---")
    prod = Produto("Teclado Mecânico", 350.00, 10)
    print(prod)        # Testa o __str__
    print(repr(prod))  # Testa o __repr__

    print("\n--- 2. Realizando Vendas ---")
    prod.vender(4)
    print(prod)

    print("\n--- 3. Realizando Reposição ---")
    prod.repor(5)
    print(prod)

    print("\n--- 4. Tentativa de Alterar Preço para Inválido ---")
    try:
        prod.preco = -10  # Deve disparar ValueError
    except ValueError as e:
        print(f"Capturado esperado: {e}")

    print("\n--- 5. Tentativa de Venda Além do Estoque ---")
    try:
        prod.vender(15)  # Restam 11 no estoque, deve disparar ValueError
    except ValueError as e:
        print(f"Capturado esperado: {e}")

    print("\n--- Estado Final do Produto ---")
    print(prod)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Parte 2: q09_resposta.txt (Explicação Teórica)
Plaintext
===============================================================================
Explicação: Diferença entre _atributo e __atributo em Python
===============================================================================

Em Python, o encapsulamento não é baseado em restrições rígidas travadas pelo 
compilador (como o 'private' e 'protected' em Java ou C++), mas sim em convenções 
de nomenclatura e no comportamento do interpretador.

1. Atributo com um underline (_atributo):
-------------------------------------------------------------------------------
* Tipo: Protegido por convenção (Protected).
* O que significa: É um aviso visual para outros desenvolvedores de que o atributo 
  ou método é de uso "interno" da classe ou de suas subclasses. Ele NÃO deve ser 
  acessado diretamente de fora da classe.
* Comportamento prático: O Python NÃO impede o acesso ou modificação direta se você 
  fizer 'objeto._atributo'. A única restrição real ocorre ao usar 'from modulo import *', 
  onde os elementos começados com '_' não são importados automaticamente.

2. Atributo com dois underlines (__atributo):
-------------------------------------------------------------------------------
* Tipo: Privado com Name Mangling (Desfiguração de Nome).
* O que significa: Indica que o atributo é estritamente privado da classe onde 
  foi criado, não devendo ser acessado nem por classes filhas (evitando colisões 
  de nomes em heranças múltiplas).
* Comportamento prático: O interpretador do Python altera ativamente o nome do 
  atributo internamente para '_NomeDaClasse__atributo'. Por conta disso, se você 
  tentar acessar 'objeto.__atributo' de fora da classe, receberá um erro de 
  'AttributeError' (o atributo parecerá não existir). 
  
* Nota: Ainda é possível burlar o sistema acessando pelo nome desfigurado 
  ('objeto._NomeDaClasse__atributo'), pois o Python preza pela liberdade do 
  desenvolvedor ("somos todos adultos consentindo aqui"), mas o duplo underline 
  impede acessos acidentais com eficiência.
