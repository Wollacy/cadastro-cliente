clientes = []

while True:
    print("\nMenu Inicial:")
    print("1. Cadastrar cliente")
    print("2. Listar clientes")
    print("3. Alterar cliente")
    print("4. Remover cliente")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Cadastrar Cliente")
        codigo = input("Digite o código do cliente: ")
        
        # Verificação para evitar códigos duplicados
        existe = False
        for cliente in clientes:
            if cliente["codigo"] == codigo:
                existe = True
                break
        if existe:
            print(f"Erro: Já existe um cliente com o código {codigo}.")
        else:
            nome = input("Digite o nome do cliente: ")
            cliente = {"codigo": codigo, "nome": nome}
            clientes.append(cliente)
            print(f"Cliente {codigo} - {nome} cadastrado com sucesso!") 
    elif opcao == "2":
        print("Listar Clientes")
        if not clientes:
            print("Nenhum cliente cadastrado.")
        else:
            for cliente in clientes:
                print(f"Código: {cliente['codigo']} - Nome: {cliente['nome']}")
    elif opcao == "3":
        print("Alterar Cliente")
        codigo = input("Digite o código do cliente que deseja alterar: ")
        
        cliente_encontrado = None
        for cliente in clientes:
            if cliente["codigo"] == codigo:
                cliente_encontrado = cliente
                break

        if cliente_encontrado:
            nome = input("Digite o novo nome do cliente: ")
            cliente_encontrado["nome"] = nome
            print(f"Cliente {codigo} alterado com sucesso!")
        else:
            print(f"Erro: Cliente com código {codigo} não encontrado.")
    elif opcao == "4":
        print("Remover Cliente")
        codigo = input("Digite o código do cliente que deseja remover: ")

        cliente_encontrado = None
        for cliente in clientes:
            if cliente["codigo"] == codigo:
                cliente_encontrado = cliente
                break

        if cliente_encontrado:
            clientes.remove(cliente_encontrado)
            print(f"Cliente {codigo} removido com sucesso!")
        else:
            print(f"Erro: Cliente com código {codigo} não encontrado.")
    elif opcao == "5":
        print("Saindo do sistema. Até mais!")
        break
    else:
        print("A opção escolhida não existe. Por favor, tente novamente.")