import subprocess
import os
import json
from datetime import datetime

def definir_horario():
    return datetime.now().strftime('%d-%m-%Y %H:%M')

def criar_log(eventos):
    data =  datetime.now().strftime('%d-%m-%Y')
    if not os.path.exists('./logs'):
        os.makedirs('logs')
        with open(f'./logs/ping-monitor_{data}.log', 'w') as arquivo:
            arquivo.write(eventos)
    else:
        with open(f'./logs/ping-monitor_{data}.log', 'a') as arquivo:
            arquivo.write(eventos)

def carregar_json() -> dict:
    file_path = input('Digite o caminho para o arquivo JSON: ').strip()
    try:
        with open(f'{file_path}') as arquivo:
            conteudo = json.load(arquivo)
            if conteudo == {}:
                print('Seu arquivo JSON está vazio.')
                raise SystemExit
            else:
                return conteudo
    except FileNotFoundError as exc:
        print(f'\nArquivo não encontrado, verifique se você digitou o caminho corretamente.\n{exc}\n')
        raise SystemExit
    except json.JSONDecodeError as exc:
        print(f'\nOcorreu um erro com o seu arquivo JSON, verifique-o e tente novamente.\n{exc}\n')
        raise SystemExit
    except Exception as exc:
        print(f'\nOcorreu um erro inesperado.\n{exc}\n')
        raise SystemExit

def pingar_servidores(servidores: dict):

    print('Verificando servidores, aguarde...')
    for nome, ip in servidores.items():
        parametro = '-n' if os.name == 'nt' else '-c'
        ping = subprocess.run(['ping', f'{parametro}','2' ,f'{ip}'], capture_output=True, text=True)
        horario = definir_horario()
        if ping.returncode == 0:
            print(f'{horario}      {nome}: {ip}       [ONLINE]')
            resultado = f'{horario}      {nome}: {ip}       [ONLINE]\n'
            criar_log(resultado)
        elif ping.returncode == 1:
            print(f'{horario}      {nome}: {ip}       [OFFLINE]')
            resultado = f'{horario}      {nome}: {ip}       [OFFLINE]\n'
            criar_log(resultado)

print('\n#### Bem-vindo ao Ping Monitor V1.0 ####')
pingar_servidores(carregar_json())
