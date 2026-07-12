# Sistema-de-Acesso-Administrativo


![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![VS Code](https://img.shields.io/badge/VS%20Code-0078d7?logo=visual-studio-code&logoColor=white)



Este é um sistema simples em Python que permite o cadastro de usuários e oferece funcionalidades restritas ao administrador. O objetivo principal é demonstrar conceitos básicos de programação, como validação de entrada, controle de fluxo e manipulação de listas.

##  Funcionalidades

- **Login Administrativo**:  
  - Acesso protegido por email e senha pré-definidos (`admin@sistema.com` / `123456`)
  - Limite de 3 tentativas antes do encerramento automático do sistema

- **Cadastro de Usuários**:  
  - Coleta nome, email (com domínio permitido), senha (mínimo 6 caracteres) e CPF (11 dígitos numéricos)
  - Validações rigorosas para evitar duplicidade ou dados inválidos

- **Visualização dos Usuários Cadastrados**:  
  - Lista todos os usuários com seus respectivos dados formatados

- **Encerramento Seguro do Sistema**

##  Tecnologias e Ferramentas Utilizadas

- **Linguagem**: Python 3.x
- **Editor de Código**: [Visual Studio Code (VS Code)](https://code.visualstudio.com/)
- **Conceitos Aplicados**:
  - Estruturas de controle: `while`, `if/else`, `for`
  - Manipulação de Listas para armazenamento temporário
  - Formatação de strings (f-strings)
  - Validação de entrada de dados

##  Como Executar

1. Certifique-se de ter o **Python** instalado na sua máquina.
2. Recomenda-se o uso do **VS Code** para editar e executar o script.
3. Clone este repositório ou baixe o arquivo `.py`.
4. Execute o script diretamente no terminal do VS Code:
   ```bash
   python funçoes_do_administrador.py

## Exemplo de Uso

=== ACESSO RESTRITO AO ADMINISTRADOR ===

Digite o email do administrador: admin@sistema.com

Digite a senha do administrador: 123456

Acesso de Administrador concedido!

Escolha uma opção:
1 - Cadastrar usuário
2 - Verificar usuários cadastrados
3 - Sair do sistema

**Desenvolvido por Kayke Augusto – Estudante de Análise e Desenvolvimento de Sistemas**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Kayke%20Augusto-0077B5?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kayke-augusto-473264413)
