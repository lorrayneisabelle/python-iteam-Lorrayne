# Desafio 08 — Banco Digital
# Aluno: Lorrayne Isabelle Paz de Oliveira
# Data:  26/05/2026

# solucao.py

class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        """
        Construtor da classe. Inicializa o titular e o saldo da conta.
        """
        self.titular = titular
        self.saldo = float(saldo_inicial)  # Atributo de instância

    def depositar(self, valor):
        """Adiciona um valor ao saldo da conta."""
        if valor > 0:
            self.saldo += valor
            print(f"💰 Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("❌ Erro: O valor do depósito deve ser maior que zero.")

    def sacar(self, valor):
        """Remove um valor do saldo, caso haja saldo suficiente."""
        if valor <= 0:
            print("❌ Erro: O valor do saque deve ser maior que zero.")
        elif valor > self.saldo:
            print(f"❌ Erro: Saldo insuficiente para sacar R$ {valor:.2f}. Saldo atual: R$ {self.saldo:.2f}")
        else:
            self.saldo -= valor
            print(f"💸 Saque de R$ {valor:.2f} realizado com sucesso!")

    def exibir_extrato(self):
        """Exibe o status atual da conta."""
        print("\n" + "="*35)
        print("         EXTRATO BANCÁRIO")
        print("="*35)
        print(f"Cliente: {self.titular}")
        print(f"Saldo Atual: R$ {self.saldo:.2f}")
        print("="*35 + "\n")


# --- TESTANDO A CLASSE (Simulação) ---
if __name__ == "__main__":
    print("--- Criando a conta do Ricardo com R$ 100,00 ---")
    conta = ContaBancaria("Ricardo", 100.0)
    
    conta.exibir_extrato()
    
    # Testando depósito
    conta.depositar(50.0)
    
    # Testando saque permitido
    conta.sacar(30.0)
    
    # Testando saque bloqueado (insuficiente)
    conta.sacar(200.0)
    
    # Mostrando resultado final
    conta.exibir_extrato()
