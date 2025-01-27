while True:
    print("\n=== Sistema de Cadastro ===")
    print("1. Cadastrar cliente")
    print("2. Listar clientes")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Opção de cadastrar cliente selecionada.")
    elif opcao == "2":
        print("Opção de listar clientes selecionada.")
    elif opcao == "3":
        print("Saindo do sistema. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")