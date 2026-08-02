import json
import ipaddress

servidores = dict()
servidores_json = dict()

def verificar_servidor(ip):
    pass

#listar servidores
def listar_servidores ():
    for i, (chave,valor) in enumerate(servidores.items()):
        print (f'{i+1}- {chave}: {valor}')
    if servidores == {}:
        print('Nenhum servidor foi adicionado!')

#pesquisar servidor
def pesquisar_servidor():
    opcao = input('Digite o nome do servidor que você quer encontrar: ').strip().lower()
    ip = servidores.get(opcao)
    if ip:
        print(f'{opcao}: {ip}')
    else:
        print('Servidor não encontrado!')

#adicionar servidor
def adicionar_servidor():
    nome_server = input('Digite o nome do servidor que você deseja adicionar: ').strip().lower()

    if nome_server in servidores:
        print('Este servidor já foi adicionado, por favor escolha outro nome.')
    else:
        ip_server = input('Digite o IP do servidor: ')
        try:
            ipaddress.ip_address(ip_server)
        except ValueError as exc:
            print(f'IP inválido! Verifique se você adicionou o IP corretamente.\n{exc}\n')
        else:
            servidores[nome_server]=ip_server
            print('Servidor adicionado com sucesso!')


#remover servidor
def remover_servidor():
    nome_server = input('Digite o nome do servidor que deseja remover: ').strip().lower()

    if nome_server in servidores:
        servidores.pop(nome_server)
        print('Servidor removido com sucesso!')
    else:
        print('Servidor não encontrado, verifique se você digitou corretamente.')

#alterar IP
def alterar_ip ():
    nome_server = input('Digite o nome do servidor que deseja alterar o IP: ').strip().lower()

    if nome_server in servidores:
        ip_server = input('Digite o novo IP do servidor: ')
        try:
            ipaddress.ip_address(ip_server)
        except ValueError as exc:
            print(f'IP inválido! Verifique se você adicionou o IP corretamente.\n{exc}\n')
        else:
            servidores[nome_server] = ip_server
            print('IP alterado com sucesso!')
    else:
        print('Este servidor não existe.')

#salvar em JSON
def salvar_em_json():
    nome_json = input('Digite um nome para o seu arquivo JSON: ').strip().lower()
    with open(f'./{nome_json}.json', 'w') as arquivo:
        json.dump(servidores, arquivo, indent=4)
    print('JSON salvo com sucesso!')

#carregar do JSON
def carregar_do_json():

    while True:
        nome_json = input('Informe o nome do arquivo JSON (sem extensão): ')
        try:
            with open(f'./{nome_json}.json') as arquivo:
                conteudo = json.load(arquivo)
                servidores.update(conteudo)
                print('Servidores carregados com sucesso!')
                break
        except FileNotFoundError as exc:
            print(f'Você precisa manter o arquivo JSON na pasta do arquivo "auditor_de_servidores.py"\n{exc}\n')

def menu_opcoes():
    print('\n##### Bem vindo ao Auditor de Servidores V1.0 #####\n')

    print('(1) - Listar Servidores\n'
          '(2) - Pesquisar Servidor\n'
          '(3) - Adicionar Servidor\n'
          '(4) - Remover Servidor\n'
          '(5) - Alterar IP do Servidor\n'
          '(6) - Salvar Servidores em JSON\n'
          '(7) - Carregar Servidores do JSON\n'
          '(8) - Exibir Menu\n'
          '(9) - Sair')


def menu():
    print('\n##### Bem vindo ao Auditor de Servidores V1.0 #####\n')

    print('(1) - Listar Servidores\n'
          '(2) - Pesquisar Servidor\n'
          '(3) - Adicionar Servidor\n'
          '(4) - Remover Servidor\n'
          '(5) - Alterar IP do Servidor\n'
          '(6) - Salvar Servidores em JSON\n'
          '(7) - Carregar Servidores do JSON\n'
          '(8) - Exibir Menu\n'
          '(9) - Sair')

    controla_menu = False
    while True:
        try:
            if not controla_menu:
                opcao = int(input('\nDigite o número da ação que você deseja realizar: '))
                controla_menu = True
            else:
                opcao = int(input('\nDigite um número para uma nova ação ou digite "8" para exibir o Menu novamente: '))
            print('')
            if 1 <= opcao <= 9:
                if opcao == 1:
                    listar_servidores()
                elif opcao == 2:
                    pesquisar_servidor()
                elif opcao == 3:
                    adicionar_servidor()
                elif opcao == 4:
                    remover_servidor()
                elif opcao == 5:
                    alterar_ip()
                elif opcao == 6:
                    salvar_em_json()
                elif opcao == 7:
                    carregar_do_json()
                elif opcao == 8:
                    menu_opcoes()
                elif opcao == 9:
                    print('Saindo... até logo!')
                    break
            else:
                print('\nOpção inválida, são permitidos apenas números de 1 a 9.\n')
        except Exception as exc:
            print(f'\nSelecione apenas números inteiros de 1 a 9.\n{exc}\n')

menu()