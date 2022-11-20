

def linha(tam = 42):
    return '-'*42


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    c = 1
    for iten in lista:
        print(f"{c} - {iten}")
        c += 1
    print(linha())
    opc = leiaInt("Escolha uma opção do menu")
    return opc


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print("ERRO: por favor digite um número inteiro válido.")
            continue
        except(KeyboardInterrupt):
            print("O usuário preferiu não digitar o valor esperado.")
            return 0
        else:
            return n


def arquivoExiste(nome):
    while True:
        try:
            a = open(nome, 'rt')
            a.close()
        except(FileNotFoundError):
            return  False
        else:
            return  True


def criarArquivo(nome):
    while True:
        try:
            a = open(nome, 'wt+')
            a.close()
        except:
            print("Houve um erro na criação do arquivo.")
        else:
            print(f"Arquivo {nome} criado com sucesso.")
            a.close()
            break


def atualizarContato():
    nomeDeletado = input("Digite o nome para ser Atualizado: ").lower()
    agenda = open("agenda.txt", "r")
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if nomeDeletado not in aux[i].lower():
            aux2.append(aux[i])
    agenda = open("agenda.txt", "w")
    for i in aux2:
        agenda.write(i)
    idContato = input("Escolha o Id do contato atualizado: ")
    nome = str(input("Escreva o nome do contato atualizado: "))
    telefone = input("Escreva o telefone do contato atualizado: ")
    email = input("Escreva o email do contato atualizado: ")
    try:
        agenda = open("agenda.txt", "a")
        dados = f'{idContato};{nome};{telefone};{email} \n'
        agenda.write(dados)
        agenda.close()
        print(f'Contato Atualizado com sucesso !!!!')
    except:
        print("ERRO na gravação do contato")


def cadastrarContato():
    idContato = leiaInt("Escolha o Id do contato: ")
    nome = str(input("Escreva o nome do contato: "))
    telefone = input("Escreva o telefone do contato: ")
    email = input("Escreva o email do contato: ")
    try:
        agenda = open("agenda.txt", "a")
        dados = f'{idContato};{nome};{telefone};{email} \n'
        agenda.write(dados)
        agenda.close()
        print(f'Contato gravado com sucesso !!!!')
    except:
        print("ERRO na gravação do contato")


def listarContato():
    agenda = open("agenda.txt", "r")
    for contato in agenda:
        print(contato)
    agenda.close()


def deletarContato():
    nomeDeletado = leiaInt("digite o número do ID a ser deletado")
    agenda = open("agenda.txt", "r")
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if nomeDeletado in agenda:
            aux2.append(aux[i])
    agenda = open("agenda.txt", "w")
    for i in aux2:
        agenda.write(i)
    print(f'contato deletado com sucesso')
    listarContato()


def buscarContatoPeloNome():
    nome = input(f'digite o nome a ser procurado: ').upper()
    agenda = open("agenda.txt", "r")
    for contato in agenda:
        if nome in contato.split(";")[1].upper():
            print(contato)
    agenda.close()


def sair():
    print(f'Até mais... !!!')
    exit()


def main(menu):
    menu()


#main()
