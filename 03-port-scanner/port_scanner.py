import socket
import time
import ipaddress


PORTAS_COMUNS = {
    'FTP-data': 20,
    'FTP': 21,
    'SSH': 22,
    'Telnet': 23,
    'SMTP': 25,
    'DNS': 53,
    'HTTP': 80,
    'POP3': 110,
    'IMAP': 143,
    'HTTPS': 443,
    'SMB': 445,
    'SMTP-submission': 587,
    'IMAPS': 993,
    'POP3S': 995,
    'MySQL': 3306
}


def testar_porta(ip: str, porta: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        soc.settimeout(1)

        try:
            soc.connect((ip, porta))
            return True
        except (ConnectionRefusedError, TimeoutError, PermissionError, OSError):
            return False


def verificar_portas(portas_abertas: list) -> None:
    quantidade = len(portas_abertas)

    if not portas_abertas:
        print('\nNão foi encontrada nenhuma porta aberta.')
    elif quantidade == 1:
        print(f'\nTotal de {quantidade} porta aberta.')
    else:
        print(f'\nTotal de {quantidade} portas abertas.')


def testar_portas(ip: str, portas: dict) -> None:
    portas_abertas = []

    print('\nTestando portas, aguarde...\n')

    inicio = time.perf_counter()

    for nome, numero in portas.items():
        if testar_porta(ip, numero):
            print(f'{nome} {numero} ...... ABERTA')
            portas_abertas.append((nome, numero))

    tempo_gasto = time.perf_counter() - inicio

    verificar_portas(portas_abertas)
    print(f'Tempo de varredura: {tempo_gasto:.2f} segundos.')


def validar_portas_manuais() -> dict:
    entrada = input(
        '\nDigite as portas desejadas '
        '(separe as portas por vírgula, ex: 20, 22, 80...): '
    )

    try:
        portas = [int(porta.strip()) for porta in entrada.split(',')]
    except ValueError:
        print('\nEntrada inválida. Digite apenas números separados por vírgula.')
        return {}

    portas_validas = {}

    for porta in portas:
        if 1 <= porta <= 65535:
            nome = next(
                (
                    nome
                    for nome, numero in PORTAS_COMUNS.items()
                    if numero == porta
                ),
                'Desconhecida'
            )

            portas_validas[nome] = porta
        else:
            print(f'\nA porta {porta} é inválida. Use valores entre 1 e 65535.')

    return portas_validas


def verificar_ip():
    try:
        entrada = input('\nDigite o IP que você deseja escanear: ')
        return ipaddress.ip_address(entrada)
    except ValueError:
        return None


def main():
    print(
        '\n########################################\n'
        '#### Bem-vindo ao Port Scanner V1.1 ####\n'
        '########################################'
    )

    ip_para_varredura = verificar_ip()

    while ip_para_varredura is None:
        print('Verifique se o IP está correto e tente novamente.')
        ip_para_varredura = verificar_ip()

    ip = str(ip_para_varredura)

    while True:
        try:
            opcao_escolhida = int(
                input(
                    '\n1 - Varredura Automática'
                    '\n2 - Varredura Manual'
                    '\n3 - EXIT\n'
                    '\nDigite o número da opção que você deseja realizar: '
                )
            )
        except ValueError:
            print('\nOpção inválida. Digite 1, 2 ou 3.')
            continue

        if opcao_escolhida == 1:
            testar_portas(ip, PORTAS_COMUNS)

        elif opcao_escolhida == 2:
            portas = validar_portas_manuais()

            if portas:
                testar_portas(ip, portas)

        elif opcao_escolhida == 3:
            break

        else:
            print('\nOpção inválida. Digite 1, 2 ou 3.')


if __name__ == '__main__':
    main()

