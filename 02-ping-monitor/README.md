# Ping Monitor

Ferramenta desenvolvida em Python para verificar a disponibilidade de servidores e dispositivos em uma rede utilizando o comando `ping`.

O programa recebe uma lista de servidores através de um arquivo JSON, realiza uma verificação de disponibilidade para cada endereço e exibe o resultado no terminal. As informações obtidas também são registradas em arquivos de log organizados por data.

> **Status:** Versão 1.0

---

## Funcionalidades

* Carregamento de servidores através de arquivo JSON
* Monitoramento de múltiplos servidores
* Verificação de disponibilidade utilizando `ping`
* Identificação de servidores online e offline
* Registro de data e horário das verificações
* Geração automática de arquivos de log
* Organização dos logs por data
* Tratamento de erros relacionados ao arquivo JSON

---

## Como funciona

O funcionamento do programa pode ser resumido nas seguintes etapas:

```text
Início
  │
  ▼
Solicita o caminho do arquivo JSON
  │
  ▼
Carrega os servidores
  │
  ▼
Percorre cada servidor
  │
  ▼
Executa o ping
  │
  ├── Responde ──────► [ONLINE]
  │
  └── Não responde ─► [OFFLINE]
                         │
                         ▼
                    Salva no log
```

### 1. Carregamento dos servidores

Ao iniciar o programa, o usuário informa o caminho para o arquivo JSON que contém os servidores que serão monitorados.

Exemplo:

```text
Digite o caminho para o arquivo JSON: servidores.json
```

O arquivo deve conter o nome de cada servidor associado ao seu endereço IP ou hostname.

Exemplo:

```json
{
    "Servidor Web": "192.168.1.10",
    "Servidor Banco": "192.168.1.20",
    "Servidor DNS": "192.168.1.30"
}
```

O módulo `json` é utilizado para ler o arquivo e converter seu conteúdo em um dicionário Python.

---

### 2. Verificação dos servidores

A função `pingar_servidores()` percorre todos os servidores carregados e executa o comando `ping` utilizando o módulo `subprocess`.

O código de retorno do comando é utilizado para determinar o resultado da verificação.

Quando o servidor responde:

```text
[ONLINE]
```

Quando o servidor não responde:

```text
[OFFLINE]
```

---

### 3. Registro de data e horário

Cada verificação recebe a data e o horário em que foi realizada.

O formato utilizado é:

```text
DD-MM-YYYY HH:MM
```

Exemplo:

```text
09-08-2026 09:35
```

Essa informação é exibida no terminal e também armazenada no arquivo de log.

---

### 4. Sistema de logs

A função `criar_log()` é responsável por registrar os resultados das verificações.

Os logs são armazenados no diretório:

```text
logs/
```

Os arquivos são organizados de acordo com a data da execução.

Exemplo:

```text
logs/
├── ping-monitor_09-08-2026
├── ping-monitor_10-08-2026
└── ping-monitor_11-08-2026
```

Caso o diretório `logs` não exista, ele é criado automaticamente.

Exemplo de conteúdo:

```text
09-08-2026 09:35      Servidor Web: 192.168.1.10       [ONLINE]
09-08-2026 09:35      Servidor Banco: 192.168.1.20      [ONLINE]
09-08-2026 09:35      Servidor DNS: 192.168.1.30        [OFFLINE]
```

---

## Estrutura do projeto

Uma possível estrutura para o projeto:

```text
02-ping-monitor/
│
├── ping_monitor.py
├── servidores.json
├── logs/
│   └── ping-monitor_DD-MM-YYYY
│
└── README.md
```

O diretório `logs/` é criado automaticamente pelo programa, portanto não é necessário criá-lo manualmente.

---

## Tecnologias utilizadas

O projeto utiliza apenas módulos da biblioteca padrão do Python:

| Módulo       | Utilização                              |
| ------------ | --------------------------------------- |
| `subprocess` | Execução do comando `ping`              |
| `os`         | Criação e verificação de diretórios     |
| `json`       | Leitura do arquivo de configuração      |
| `datetime`   | Obtenção e formatação de data e horário |

Não são necessárias bibliotecas externas.

---

## Requisitos

* Python 3
* Sistema operacional com o comando `ping` disponível

O programa utiliza o comando `ping` fornecido pelo próprio sistema operacional.

---

## Execução

Clone o repositório ou baixe os arquivos do projeto.

Execute o programa:

```bash
python ping_monitor.py
```

Em sistemas onde o Python 3 é chamado pelo comando `python3`:

```bash
python3 ping_monitor.py
```

Ao iniciar, o programa solicitará o caminho do arquivo JSON:

```text
#### Bem-vindo ao Ping Monitor V1.0 ####

Digite o caminho para o arquivo JSON:
```

Informe o arquivo contendo os servidores que deseja verificar.

---

## Configuração do JSON

O arquivo JSON deve seguir uma estrutura de chave e valor:

```json
{
    "Servidor Web": "192.168.1.10",
    "Servidor Banco": "192.168.1.20",
    "Servidor DNS": "192.168.1.30"
}
```

A chave representa o nome do servidor e o valor representa o endereço que será utilizado no comando `ping`.

Também é possível utilizar hostnames, desde que sejam resolvidos corretamente pelo sistema:

```json
{
    "Servidor Web": "server-web",
    "Servidor Banco": "server-db"
}
```

---

## Tratamento de erros

O programa possui tratamento para algumas situações que podem ocorrer durante a execução.

### Arquivo não encontrado

Caso o caminho informado não corresponda a um arquivo existente:

```text
Arquivo não encontrado, verifique se você digitou o caminho corretamente.
```

### JSON inválido

Caso o arquivo possua uma estrutura JSON inválida:

```text
Ocorreu um erro com o seu arquivo JSON, verifique-o e tente novamente.
```

### JSON vazio

Caso o arquivo contenha um objeto vazio:

```text
Seu arquivo JSON está vazio.
```

Também existe um tratamento genérico para outros erros inesperados durante o carregamento do arquivo.

---

## Exemplo de execução

```text
#### Bem-vindo ao Ping Monitor V1.0 ####

Digite o caminho para o arquivo JSON: servidores.json

Verificando servidores, aguarde...

09-08-2026 09:35      Servidor Web: 192.168.1.10       [ONLINE]
09-08-2026 09:35      Servidor Banco: 192.168.1.20      [ONLINE]
09-08-2026 09:35      Servidor DNS: 192.168.1.30        [OFFLINE]
```

Os mesmos resultados serão registrados no arquivo de log correspondente à data da execução.

---

## Objetivo do projeto

O Ping Monitor foi desenvolvido como uma ferramenta simples para verificar a disponibilidade de servidores e, ao mesmo tempo, praticar conceitos relacionados à programação em Python e administração de sistemas.

O projeto envolve conceitos como:

* Manipulação de arquivos
* Estruturas de dados
* JSON
* Tratamento de exceções
* Execução de comandos do sistema
* Monitoramento de rede
* Geração e organização de logs
* Manipulação de data e horário

---

## Limitações atuais

A versão atual realiza **uma única rodada de verificações**. Após verificar todos os servidores, o programa é encerrado.

Apesar do nome "Ping Monitor", ele ainda não realiza monitoramento contínuo.

Uma evolução natural do projeto seria implementar um ciclo de monitoramento com intervalo configurável entre as verificações, permitindo acompanhar continuamente o estado dos servidores.

---
