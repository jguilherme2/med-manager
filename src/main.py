from manager import adicionar, listar

def menu():
    print("\n=== GERENCIADOR DE MEDICAMENTOS ===")
   print("1 - Cadastrar medicamento")
print("2 - Listar medicamentos")
print("3 - Marcar como tomado")
print("4 - Sair")

def main():
    while True:
        menu()
        op = input("Escolha: ")

        if op == "1":
            nome = input("Nome: ")
            horario = input("Horário: ")
            adicionar(nome, horario)
            print("Medicamento cadastrado!")

       elif op == "2":
    meds = listar()
    if not meds:
        print("Nenhum medicamento cadastrado.")
    for i, m in enumerate(meds):
        status = "✔" if m["tomado"] else "✘"
        print(f"{i} - {m['nome']} ({m['horario']}) [{status}]")

        elif op == "3":
    meds = listar()

    if not meds:
        print("Nenhum medicamento cadastrado.")
        continue

    for i, m in enumerate(meds):
        print(f"{i} - {m['nome']}")

    try:
        idx = int(input("Escolha o número: "))
        meds[idx]["tomado"] = True

        from manager import salvar
        salvar(meds)

        print("Medicamento marcado como tomado!")

    except:
        print("Entrada inválida")

elif op == "4":
    break

        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()