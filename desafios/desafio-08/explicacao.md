# Explicação — Desafio 08 — Banco Digital

# Explicação — Desafio 08 — Banco Digital

**Aluno:** Lorrayne Isabelle Paz de Oliveira
**Data:** 26 de Maio de 2026  

## O que meu programa faz

O programa aplica os conceitos iniciais de **Programação Orientada a Objetos (POO)** para simular o funcionamento de uma conta corrente:
* **Criação de Contas:** Permite instanciar objetos "Conta" únicos, onde cada um possui seu próprio dono (titular) e uma quantia em dinheiro (saldo).
* **Movimentações Financeiras:** Através de métodos específicos, simula a entrada (`depositar`) e a saída (`sacar`) de dinheiro.
* **Validação de Segurança:** O método de saque possui uma estrutura condicional (`if/else`) que impede a operação caso o usuário tente sacar um valor maior do que o saldo disponível, evitando que a conta fique negativa.
* **Consulta:** O método `exibir_extrato` exibe um resumo organizado com o nome do cliente e o saldo atualizado.

## Resposta à Pergunta Obrigatória

> Por que saldo deve ser um atributo da instância (self.saldo) e não uma variável comum dentro do método? O que mudaria no comportamento do programa?

O saldo deve ser um atributo da instância (`self.saldo`) porque ele representa o **estado** do objeto, algo que precisa ser lembrado e mantido durante toda a vida útil daquela conta. O prefixo `self` indica que a variável pertence ao objeto e pode ser acessada ou modificada por **qualquer método** dentro da classe a qualquer momento.

Se usássemos uma variável comum dentro de um método (por exemplo, apenas `saldo = valor` dentro de `depositar`), duas coisas mudariam drasticamente no comportamento do programa:

1. **Perda de memória (Escopo Local):** A variável seria criada quando o método fosse chamado e **destruída** assim que o método terminasse de rodar. O dinheiro "sumiria" da memória logo após o depósito.
2. **Isolamento de dados:** Os outros métodos não conseguiriam ver essa variável. O método `sacar` ou o `exibir_extrato` não teriam acesso ao valor guardado no método `depositar`, resultando em um erro de código (`NameError`) ou na impossibilidade de atualizar o saldo global da conta.

## Dificuldades encontradas
A maior virada de chave nesse desafio foi entender o papel do `self`. No início, é confuso entender por que precisamos escrever `self.saldo` e `self.titular` em todas as linhas dentro da classe, em vez de apenas usar variáveis normais. 
Após ver o comportamento dos métodos isolados, ficou claro que o `self` funciona como o "endereço" que conecta as ações (métodos) às características (atributos) do objeto. Também exigiu atenção a tipagem dos dados no construtor, garantindo a conversão do saldo inicial para `float` para que operações matemáticas com casas decimais funcionassem perfeitamente sem gerar erros de tipo.
