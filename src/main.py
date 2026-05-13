from api_service import buscar_medicamento


def menu():
    print("1 - Cadastrar medicamento")
    print("2 - Listar medicamentos")
    print("3 - Buscar medicamento na API")
    print("0 - Sair")


def main():

    while True:
        menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Cadastro em desenvolvimento")

        elif opcao == "2":
            print("Listagem em desenvolvimento")

        elif opcao == "3":
            nome = input("Digite o nome do medicamento: ")

            resultado = buscar_medicamento(nome)

            if resultado:
                print("Medicamento encontrado!")
                print(resultado)
            else:
                print("Medicamento não encontrado.")

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida")


if __name__ == "__main__":
    main()