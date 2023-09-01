campos = {'Nome': "",
          'Idade': 0,
          'Altura': 0.00,
          'Profissão': ""}
escolha_menu = 1


def exibir_campos(camp):
    for k, v in camp.items():
        print(f"{k}: {v}")


def inserir_campo(camp) -> dict:
    nv_campo = input("Qual campo deseja adicionar? ")
    try:
        nv_campo = int(nv_campo)
        camp[nv_campo] = int(input("Digite o valor do campo: "))
    except ValueError:
        try:
            nv_campo = float(nv_campo)
            camp[nv_campo] = float(input("Digite o valor do campo: "))
        except ValueError:
            camp[nv_campo] = input("Digite o valor do campo: ")
    print(f"Campo {nv_campo} com o valor {camp[nv_campo]} adicionado.")
    return camp


def menu_campos(camp):
    i = 0
    for k in camp.keys():
        i += 1
        print(f"{i} - {k}")


def alterar_campo(camp) -> dict:
    escolha_campo = int(input("Digite o campo que deseja alterar: "))
    match escolha_campo:
        case 1:
            camp['Nome'] = input("Nome: ")
        case 2:
            camp['Idade'] = int(input("Idade: "))
        case 3:
            camp['Altura'] = float(input("Altura: "))
        case 4:
            camp['Profissão'] = input("Profissão: ")
    return camp


def exibir_campo_espec(camp):
    escolha_campo = int(input("Digite o campo que deseja exibir: "))
    match escolha_campo:
        case 1:
            print(f"Nome: {camp['Nome']}")
        case 2:
            print(f"Idade: {camp['Idade']}")
        case 3:
            print(f"Altura: {camp['Altura']}")
        case 4:
            print(f"Profissão: {camp['Profissão']}")
    return camp


def remover_campo(camp) -> dict:
    escolha_campo = int(input("Digite o campo que deseja excluir: "))
    match escolha_campo:
        case 1:
            del camp['Nome']
            print("Campo: Nome - excluído.")
        case 2:
            del camp['Idade']
            print("Campo: Idade - excluído.")
        case 3:
            del camp['Altura']
            print("Campo: Altura - excluído.")
        case 4:
            del camp['Profissão']
            print("Campo: Profissão - excluído.")
    return camp


print("Antes de começar, você deve preencher os campos iniciais: ")
campos['Nome'] = input("Digite o nome: ")
campos['Idade'] = int(input("Digite a idade: "))
campos['Altura'] = float(input("Digite a altura: "))
campos['Profissão'] = input("Digite sua profissão: ")
print("""
   MENU
1 - Exibir campos
2 - Inserir campo
3 - Alterar valor de campo
4 - Exibir um campo específico
5 - Remover um campo específico
0 - SAIR
""")
escolha_menu = int(input("Selecione uma opção: "))
match escolha_menu:
    case 0:
        print("Finalizando programa...")
    case 1:
        exibir_campos(campos)
    case 2:
        campos = inserir_campo(campos)
    case 3:
        menu_campos(campos)
        campos = alterar_campo(campos)
    case 4:
        menu_campos(campos)
        exibir_campo_espec(campos)
    case 5:
        menu_campos(campos)
        campos = remover_campo(campos)
    case _:
        print("Digite um valor válido...")
print("\nDicionário final:")
exibir_campos(campos)
