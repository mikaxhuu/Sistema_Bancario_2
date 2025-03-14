# Sistema_Bancario_2
  Realização de um projeto avançado proposto pela plataforma dio.me do Bootcamp de Python, baseado em um [modelo](https://github.com/digitalinnovationone/trilha-python-dio/blob/main/00%20-%20Fundamentos/desafio.py) mais simples, com objetivo de incrementar mais funcionalidades complexas a ele.

## Objetivo geral:

  Separar as funções existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar usuário(cliente) e cadastrar conta bancária.

## Desafio:

  Precisamos deixar nosso código mais modularizado, para isso vamos criar duas funções para as operações existentes: **sacar**, **depositar** e **visualizar histórico**. Além disso, para a versão 2 do nosso sistema precisamos criar duas novas funções: **criar usuário (cliente do banco)** e **criar conta corrente (vincular com o usuário)**.

## Separação em funções:

  Devemos criar funções para todas as operações do sistema. Para exercitar tudo o que aprendemos neste módulo, cada função vai ter uma regra na passagem de argumentos. O retorno e a forma como serão chamadas, pode ser definida por você como achar melhor.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# **Saque**
  *A função saque deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestão de retorno: saldo e extrato.*

# **Depósito**
  *A função deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.*

# **Extrato**
  *A função de extrato deve receber os argumentos por posição e nome (positional only e keyword only). Argumentos posicionais: saldo, Argumentos nomeados: extrato.*


# **Novas funções:**

  Precisamos criar duas novas funções: criar usuário e criar conta corrente. Fique a vontade para adicionar mais funções, exemplo: listar contas.

## **Criar usuário (cliente)**
  *O programa deve armazenar os usuários em uma lista, um usuário é composto por:*
  - **Nome, data de nascimento, cpf e endereço.**
  
  *O endereço é uma string com o formato:*
  - **Logradouro, número - bairro - cidade/sigla, estado.**

  *Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.*

## **Criar conta corrente**
  *O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e o usuário. O número da conta é sequencial, iniciando em 1.*
  *O número da agência fixo é "0001".*
  *O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.*

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# **Dica**

  Para vincular um usuário e uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.
