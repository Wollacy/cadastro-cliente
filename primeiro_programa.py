def menu():
    print("Sistema de Cadastro de Clientes")
    print("1. Cadastrar cliente")
    print("2. Listar clientes")
    print("3. Editar cliente")
    print("4. Excluir cliente")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")
    return opcao

opcao = menu()
if opcao.isdigit():
    opcao = int(opcao)
    if 1 <= opcao <= 5:
        print(f"Você escolheu a opção {opcao}")
    else:
        print("Opção inválida!")
else:
    print("Por favor, digite um número válido.")

