import json


def principal():
    while True:
        print(" === Agenda Telefônica === ")
        print(" 1- Criar contato")
        print(" 2- Alterar contato")
        print(" 3- Remover contato")
        print(" 4- Pesquisar contato")
        print(" 5- Listar contatos")
        print(" 6- Sair")

        opcao = input(" > ")
        if opcao not in '123456':
            print('Opção inválida. Insira um numero da lista.')
        elif opcao == '1':
            criar_contatos()
        elif opcao == '2':
            alterar()
        elif opcao == '3':
            remover()
        elif opcao == '4':
            pesquisar()
        elif opcao == '5':
            listar()
        elif opcao == '6':
            print("Saindo da agenda...")
            break


def criar_contato():
    contatos = abrir_agenda()
    lista_nome = list(contatos.keys())
    nome = input('Digite um nome: ')
    while nome.lower() in mudar_minuscula(lista_nome):
        print(f'{nome} já está cadastrado. Digite outro nome')
        nome = input("Digite um nome: ")

    email = input("Digite um email: ")
    while not validar_email(email):
        print(f'O email [{email}] tá errado bota email certo pfv!')
        email = input('Digite um novo email: ')

    telefone = input("Digite um telefone, números só: ")
    while not validar_telefone(telefone):
        print(f'O telefone [{telefone}] tá errado bota telefone certo pfv!')
        telefone = input("Digite um telefone: ")

    twitter = input("Digite um Twitter: ")
    instagram = input("Digite um Instagram: ")

    contato = {
        nome: {
            "email": email,
            "telefone": telefone,
            "twitter": twitter,
            "instagram": instagram
        }
    }
    contatos.update(contato)
    print(f"O contato {nome} foi cadastrado com sucesso!")

    salvar_arquivo(contatos)


def mudar_minuscula(lista):
    for nome in range(len(lista)):
        lista[nome] = lista[nome].lower()
    return lista


def criar_contatos():
    while True:
        try:
            quantidade_contatos = input('Quantidade de contatos a criar: ')
            for contato in range(int(quantidade_contatos)):
                criar_contato()
            principal()
        except ValueError:
            print("Caracter inválido!! Digite um número por favor!!")


def alterar():
    nome = input('Digite o nome a ser alterado: ')
    contatos = abrir_agenda()
    contato_alterado = False
    try:
        for chave in contatos.copy():
            if chave.lower() == nome.lower():
                nome = input("Digite um novo nome: ")
                lista_nome = list(contatos.keys())
                while nome in mudar_minuscula(lista_nome):
                    print(f'O contato {nome} já existe. Digite outro')
                    nome = input('Digite um nome: ')
                email = input('Digite um novo email: ')
                while validar_email(email):
                    print(f'O email [{email}] tá errado bota email certo pfv!')
                    email = input('Digite um novo email: ')
                telefone = input('Digite um novo telefone, números só: ')
                while not validar_telefone(telefone):
                    print(f'O telefone [{telefone}] tá errado bota telefone certo pfv!')
                    telefone = input("Digite um telefone: ")

                twitter = input('Digite um novo Twitter: ')
                instagram = input('Digite um novo Instagram: ')

                contatos.copy()[chave]['email'] = email
                contatos.copy()[chave]['telefone'] = telefone
                contatos.copy()[chave]['twitter'] = twitter
                contatos.copy()[chave]['instagram'] = instagram

                contatos[nome] = contatos.pop(chave)
                salvar_arquivo(contatos)
                contato_alterado = True
                print(f'O contato {nome} foi atualizado com sucesso!!')

        if contato_alterado == False:
            print('Contato inexistente!')
    except AttributeError:
        print('Contato inexistente!!')


def remover():
    nome = input('Digite um nome: ')
    contatos = procura_contato_em_arquivo(nome)

    try:
        for nome in contatos.keys():
            pass
        contatos.pop(nome)
        print(f'O contato {nome} foi removido com sucesso!')
        salvar_arquivo(contatos)
    except AttributeError:
        print(f'O contato {nome} não existe!!')


def pesquisar():
    nome = input('Digite um nome: ')
    contato = procura_contato_em_arquivo(nome)
    imprimir_contato(contato)


def listar():
    contatos = abrir_agenda()
    if len(contatos) == 0:
        return print('Não existem contatos cadastrados!!')
    imprimir_contato(contatos)


def abrir_agenda():
    try:
        with open('agenda_telefonica.json', encoding='utf-8') as meu_json:
            contatos = json.load(meu_json)
        return contatos
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return {}


def imprimir_contato(contato):
    try:
        for nome, valor in contato.items():
            print('-------------------------\n'
                  f'nome: {nome}\n'
                  f'email: {valor["email"]}\n'
                  f'telefone: {valor["telefone"]}\n'
                  f'Twitter: {valor["twitter"]}\n'
                  f'Instagram: {valor["instagram"]}\n'
                  '-------------------------')
    except AttributeError:
        print(f"Contato não encontrado!! Tente novamente!!")


def salvar_arquivo(contatos):
    arquivo = open('agenda_telefonica.json', 'w')
    json.dump(contatos, arquivo)
    arquivo.close()


def procura_contato_em_arquivo(nome):
    contatos = abrir_agenda()

    for contato, valor in contatos.items():
        if contato.lower() == nome.lower():
            return {contato: valor}
        if contato == '':
            return {}


def validar_email(email):
    import re

    formato = '^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$'
    if re.match(formato, email):
        return True
    return False


def validar_telefone(telefone):
    try:
        int(telefone)
        return True
    except ValueError:
        return False

principal()
