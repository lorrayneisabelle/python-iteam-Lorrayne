# Explicação — Desafio 09 — Sistema de Frota

**Aluno:** Lorrayne Isabelle Paz de Oliveira
**Data:** 26/05/2026
# Explicação — Desafio 09 — Sistema de Frota

## O que meu programa faz

O programa implementa conceitos avançados de POO para gerenciar veículos em um sistema de frota de forma organizada:
* **Herança:** Criamos uma classe base `Veiculo` que centraliza o que todo transporte tem em comum (marca, ano e quilometragem), evitando repetição de código nas classes `Caminhao` e `Moto`.
* **Polimorfismo:** O método `exibir_dados()` existe na classe pai e foi sobrescrito nas classes filhas. Ao utilizarmos o `super()`, a filha aproveita o comportamento original do pai e apenas adiciona suas particularidades (como toneladas ou cilindradas).
* **Encapsulamento:** O atributo `__quilometragem` recebeu o prefixo de duplo sublinhado, tornando-o privado. Isso impede que o saldo de quilômetros seja alterado diretamente por fora da classe (ex: `veiculo.__quilometragem = -500`), forçando o uso do método controlado `rodar(km)`.
## Resposta à Pergunta Obrigatória

> Por que Caminhao e Moto 'herdam de' Veiculo e não simplesmente repetem os atributos? O que você ganha e o que arrisca ao usar herança?

Eles herdam de `Veiculo` porque compartilham uma relação de tipo: um Caminhão **é um** Veículo, assim como uma Moto **é um** Veículo. Repetir os atributos em cada classe isolada violaria o princípio de design de software conhecido como **DRY (Don't Repeat Yourself)**. O que você GANHA:
* **Reaproveitamento de Código:** Escrevemos a lógica de marca, ano e movimentação (`rodar`) apenas uma vez. Qualquer melhoria feita em `Veiculo` é aplicada instantaneamente em todas as filhas.
* **Polimorfismo e Extensibilidade:** Se amanhã precisarmos criar a classe `Carro`, basta herdá-la de `Veiculo`. Além disso, podemos colocar caminhões, motos e carros em uma única lista e tratar todos genericamente como "Veículos", chamando o mesmo método `exibir_dados()`.
O que você ARRISCA:
* **Acoplamento Forte:** As classes filhas ficam intimamente ligadas à classe pai. Se fizermos uma alteração drástica ou quebrarmos algo no construtor de `Veiculo`, todas as dezenas de classes filhas podem quebrar em efeito cascata.
* **Herança Indesejada (Problema da Banana-Macaco):** Às vezes, ao herdar uma classe inteira para usar apenas um método ou atributo dela, você acaba trazendo "de brinde" comportamentos e dependências do pai que a classe filha não precisava ou não deveria ter, inflando o código sem necessidade.

Dificuldades encontradas
A maior complexidade foi alinhar o uso do `super()` com o encapsulamento. Como o atributo `__quilometragem` é estritamente privado da classe `Veiculo`, as classes filhas `Caminhao` e `Moto` não conseguem acessá-lo diretamente (o Python aplica o *name mangling*). 

Para resolver isso de forma elegante, compreendi que a melhor abordagem era fazer o método `exibir_dados()` do pai retornar a string já com a quilometragem formatada. Dessa forma, as classes filhas apenas capturam o retorno dessa string via `super().exibir_dados()` e concatenam seus atributos específicos, respeitando perfeitamente as barreiras de privacidade do encapsulamento.
