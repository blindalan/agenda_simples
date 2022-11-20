
from sistema_principal.__init import *
from time import sleep

arq='agenda.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

cabecalho("Agenda eletrônica.")

while True:
    resposta = menu([
        'cadastrar contato',
        'listar contatos',
        'Buscar contato pelo nome',
        'atualizar contato',
        'excluir contato',
        'sair da agenda'
    ])

    if resposta == 1:
        cabecalho("Cadastro de contato.")
        cadastrarContato()
        print(linha())
    elif resposta == 2:
        listarContato()
        print(linha())
    elif resposta == 3:
        buscarContatoPeloNome()
        print(linha())
    elif resposta == 4:
        atualizarContato()
        print(linha())
    elif resposta == 5:
        deletarContato()
        print(linha())
    elif resposta == 6:
        print('saindo da agenda, até logo!')
        break
    else:
        print("Erro: por favor digite um valor correspondente ao menu.")

    sleep(2)

