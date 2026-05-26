#Receba dois números do usuário, sendo a data de nascimento e o ano atual, e calcule a idade da pessoa.
nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

#Calcula a idade
idade = ano_atual - nascimento

#Exibe o resultado
print(f"A idade é: {idade}") 
