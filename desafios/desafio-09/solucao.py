# solucao.py

class Veiculo:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano
        # Atributo privado (Encapsulamento)
        self.__quilometragem = 0

    def rodar(self, km):
        """Método público para interagir com o atributo privado."""
        if km > 0:
            self.__quilometragem += km
            print(f"🛣️ O veículo rodou mais {km} km.")
        else:
            print("❌ Erro: A quilometragem inserida deve ser maior que zero.")

    def exibir_dados(self):
        """Método que será estendido pelas classes filhas."""
        return f"Marca: {self.marca} | Ano: {self.ano} | KM: {self.__quilometragem}"


class Caminhao(Veiculo):
    def __init__(self, marca, ano, capacidade_carga):
        # super() herda os atributos da classe pai
        super().__init__(marca, ano)
        self.capacidade_carga = capacidade_carga  # Atributo específico

    def exibir_dados(self):
        # super() aproveita o comportamento do método pai e adiciona o novo dado
        dados_base = super().exibir_dados()
        return f"🚚 [Caminhão] {dados_base} | Carga: {self.capacidade_carga} Toneladas"


class Moto(Veiculo):
    def __init__(self, marca, ano, cilindradas):
        super().__init__(marca, ano)
        self.cilindradas = cilindradas  # Atributo específico

    def exibir_dados(self):
        dados_base = super().exibir_dados()
        return f"🏍️ [Moto] {dados_base} | Cilindradas: {self.cilindradas}cc"


# --- SIMULAÇÃO DA FROTA (Polimorfismo em ação) ---
if __name__ == "__main__":
    print("--- Inicializando a Frota ---")
    
    # Criando instâncias das classes filhas
    scania = Caminhao("Scania", 2022, 45)
    honda = Moto("Honda", 2024, 250)
    
    # Usando o método herdado e protegido da classe pai
    scania.rodar(150)
    honda.rodar(50)
    
    print("\n--- Relatório da Frota (Polimorfismo) ---")
    frota = [scania, honda]
    
    # O mesmo método exibe comportamentos diferentes para cada objeto
    for veiculo in frota:
        print(veiculo.exibir_dados())
