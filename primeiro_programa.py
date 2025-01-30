import banco
import funcoes

banco.criar_tabela()

# Menu interativo
while True:
    print("\nMenu Inicial:")
    print("1. Cadastrar cliente")
    print("2. Listar clientes")
    print("3. Alterar cliente")
    print("4. Remover cliente")
    print("5. Buscar cliente")
    print("0. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\nCadastrar Cliente\n")
        codigo = input("Digite o código do cliente: ")
        nome = input("Digite o nome do cliente: ")
        funcoes.cadastrar_cliente(codigo, nome)
    elif opcao == "2":
        print("\nListar Clientes\n")
        funcoes.listar_clientes()
    elif opcao == "3":
        print("\nAlterar Cliente\n")
        codigo = input("Digite o código do cliente que deseja alterar: ")
        novo_nome = input("Digite o novo nome do cliente: ")
        funcoes.alterar_cliente(codigo, novo_nome)
    elif opcao == "4":
        print("\nRemover Cliente\n")
        codigo = input("Digite o código do cliente que deseja remover: ")
        funcoes.remover_cliente(codigo)
    elif opcao == "5":
        print("\nBuscar Cliente\n")
        termo = input("Digite o código ou nome do cliente: ")
        funcoes.buscar_cliente(termo)
    elif opcao == "0":
        print("\nSaindo do sistema. Até mais!\n")
        break
    else:
        print("\nA opção escolhida não existe. Por favor, tente novamente.")
