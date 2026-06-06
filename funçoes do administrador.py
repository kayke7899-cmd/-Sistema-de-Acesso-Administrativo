
# Listas para armazenar os dados dos USUÁRIOS
nome_cadastro = []
email_cadastro = []
senha_cadastro = []
cpf_cadastro = []

# Listas para armazenar os dados do ADMINISTRADOR
email_administrador = ["admin@sistema.com"]
senha_administrador = ["123456"]

# --- LOGIN DO ADMINISTRADOR ---
print("\n=== ACESSO RESTRITO AO ADMINISTRADOR ===")
tentativas_admin = 0
max_tentativas = 3
acesso_permitido = False

while tentativas_admin < max_tentativas:
    email_admin = input("Digite o email do administrador: ")
    senha_admin = input("Digite a senha do administrador: ")
    
    # Validação básica
    if email_admin == "" or senha_admin == "":
        print("Campos não podem estar vazios.")
        tentativas_admin += 1
        continue
        
    # Verifica credenciais
    if email_admin in email_administrador and senha_admin in senha_administrador:
         # Verificação rigorosa pelo índice
         idx_email = email_administrador.index(email_admin)
         idx_senha = senha_administrador.index(senha_admin)
         
         if idx_email == idx_senha:
             print("Acesso de Administrador concedido!")
             acesso_permitido = True
             break
         else:
             print("Credenciais incompatíveis.")
             tentativas_admin += 1
    else:
        print("Email ou senha de administrador incorretos.")
        tentativas_admin += 1
    
    if tentativas_admin < max_tentativas:
        print(f"Tentativa {tentativas_admin + 1} de {max_tentativas}")

if not acesso_permitido:
    print("Número máximo de tentativas excedido. Encerrando sistema.")
    exit()

# --- LOOP PRINCIPAL DO SISTEMA ---
continuar_sistema = True

while continuar_sistema:
    # Menu de opções atualizado (apenas 3 opções)
    opcao_1 = "1 - Cadastrar usuário"
    opcao_2 = "2 - Verificar usuários cadastrados"
    opcao_3 = "3 - Sair do sistema"
    
    opcao = input(f"\n{opcao_1}\n{opcao_2}\n{opcao_3}\nEscolha uma opção: ")
    
    # Opção 1: Cadastro
    if opcao == "1":
        nome = input("Digite o nome: ")
        
        # Validação do email
        while True:
            email = input("Digite o email: ")
            if email == "":
                print("O email não pode estar vazio")
                continue
            if "@gmail.com" not in email and "@hotmail.com" not in email and "@outlook.com" not in email:
                print("Formato de email inválido")
                continue
            elif email in email_cadastro:
                print("Email já cadastrado. Digite outro email.")
                continue
            else:
                break 
        
        # Validação da senha
        while True:
            senha = input("Digite a senha: ")
            if senha == "":
                print("O campo senha não pode estar vazio")
                continue
            if len(senha) < 6:
                print("A senha deve conter no mínimo 6 caracteres")
                continue
            else:
                break
        
        # Validação do CPF
        while True:
            cpf = input("Digite o CPF: ")
            if cpf == "":
                print("O CPF não pode estar vazio")
                continue
            if len(cpf) != 11 or not cpf.isdigit():
                print("CPF inválido, deve conter 11 dígitos numéricos")
                continue
            elif cpf in cpf_cadastro:
                print("CPF já cadastrado. Digite outro CPF.")
                continue
            else:
                break
        
        if nome == "":
            print("Preencha todos os campos para realizar o cadastro")
            continue
        
        # Verifica duplicidade total
        usuario_ja_existe = False
        for i in range(len(nome_cadastro)):
            if (nome_cadastro[i] == nome and 
                email_cadastro[i] == email and 
                cpf_cadastro[i] == cpf):
                usuario_ja_existe = True
                break
        
        if usuario_ja_existe:
            print("Este usuário já está completamente cadastrado.")
            continue
        
        nome_cadastro.append(nome)
        email_cadastro.append(email)
        senha_cadastro.append(senha)
        cpf_cadastro.append(cpf)
        print("Cadastro realizado com sucesso!")
    
    # Opção 2: Verificar Usuários
    elif opcao == "2":
        print("\n--- LISTA DE USUÁRIOS CADASTRADOS ---")
        if len(nome_cadastro) == 0:
            print("Nenhum usuário cadastrado no sistema.")
        else:
            for i in range(len(nome_cadastro)):
                print(f"Usuário {i+1}:")
                print(f"  Nome: {nome_cadastro[i]}")
                print(f"  Email: {email_cadastro[i]}")
                # Formata o CPF para ficar mais legível
                cpf_formatado = f"{cpf_cadastro[i][:3]}.{cpf_cadastro[i][3:6]}.{cpf_cadastro[i][6:9]}-{cpf_cadastro[i][9:]}"
                print(f"  CPF: {cpf_formatado}")
                print("-----------------------")
    
    # Opção 3: Sair
    elif opcao == "3":
        print("Saindo do sistema...")
        break
    
    # Opção Inválida
    else:
        print("Opção inválida")


      


        