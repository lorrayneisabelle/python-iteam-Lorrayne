# solucao.py
import funcoes_mat

def exibir_menu():
    print("\n" + "="*35)
    print("      📐 BIO-CALCULADORA 🧪")
    print("="*35)
    print("[1] Calcular Área do Círculo")
    print("[2] Calcular Volume de Esfera")
    print("[3] Calcular Hipotenusa")
    print("[0] Sair do Programa")
    print("="*35)

while True:
    exibir_menu()
    opcao = input("Escolha uma opção (0-3): ").strip()
    
    if opcao == "0":
        print("\nEncerrando a Bio-Calculadora. Até logo!")
        break
        
    elif opcao == "1":
        r = float(input("\nDigite o raio do círculo: "))
        resultado = funcoes_mat.area_circulo(r)
        print(f"👉 A área do círculo é: {resultado:.2f}")
        
    elif opcao == "2":
        r = float(input("\nDigite o raio da esfera: "))
        resultado = funcoes_mat.volume_esfera(r)
        print(f"👉 O volume da esfera é: {resultado:.2f}")
        
    elif opcao == "3":
        ca = float(input("\nDigite o valor do Cateto A: "))
        cb = float(input("\nDigite o valor do Cateto B: "))
        resultado = funcoes_mat.calcular_hipotenusa(ca, cb)
        print(f"👉 A hipotenusa é: {resultado:.2f}")
        
    else:
        print("\n❌ Opção inválida! Tente novamente.")
