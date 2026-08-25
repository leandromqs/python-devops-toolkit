# Port Scanner

Um port scanner TCP desenvolvido em Python para **estudar e praticar a linguagem Python**, utilizando como contexto prático conceitos relacionados a sockets, conexões TCP e portas de rede.

> **Este projeto foi desenvolvido exclusivamente para fins de estudo da linguagem Python.**

---

## 📌 Sobre o projeto

O objetivo deste projeto é utilizar a construção de uma ferramenta simples como forma de praticar Python em um cenário real.

O scanner utiliza a biblioteca padrão `socket` para tentar estabelecer conexões TCP com portas específicas e identificar quais delas aceitam uma conexão.

O projeto permite:

* Validar um endereço IP informado pelo usuário.
* Realizar uma varredura automática de portas TCP comuns.
* Realizar uma varredura manual informando portas específicas.
* Identificar portas que aceitam uma conexão TCP.
* Definir um timeout para as tentativas de conexão.
* Exibir o tempo total utilizado na varredura.
* Informar a quantidade de portas abertas encontradas.

A ferramenta foi mantida propositalmente simples, sem dependências externas ou estruturas desnecessariamente complexas.

---

## ⚙️ Como funciona

O funcionamento básico do programa pode ser representado da seguinte maneira:

```text
Usuário
   │
   ├── Informa o IP
   │
   ▼
Validação do IP
   │
   ▼
Escolha do tipo de varredura
   │
   ├── Automática
   │       │
   │       ▼
   │   Portas comuns
   │
   └── Manual
           │
           ▼
      Portas informadas
           │
           ▼
      Criar socket TCP
           │
           ▼
        connect()
           │
      ┌────┴────┐
      │         │
   Sucesso    Falha
      │         │
      ▼         ▼
   Aberta    Não aberta
```

A ferramenta utiliza uma abordagem conhecida como **TCP Connect Scan**.

Em vez de construir manualmente pacotes TCP, o programa utiliza a chamada `connect()` fornecida pelo socket TCP do sistema operacional.

---

## 🧠 Conceitos praticados

O projeto foi desenvolvido para praticar principalmente conceitos da linguagem Python, incluindo:

### Python

* Funções
* Parâmetros e retorno
* Dicionários
* Listas
* Tuplas
* Loops
* Condicionais
* Tratamento de exceções
* Context managers (`with`)
* Type hints
* Módulos da biblioteca padrão

O desenvolvimento da ferramenta também proporciona um contexto prático para compreender conceitos básicos relacionados a:

* Sockets
* TCP
* Endereçamento IP
* Portas
* Conexões de rede
* Timeout

Esses conceitos de rede são utilizados como **contexto para o estudo de Python**, e não como objetivo principal do projeto.

---

## 🛠️ Tecnologias utilizadas

* **Python 3**
* `socket`
* `ipaddress`
* `time`

Todas as bibliotecas utilizadas fazem parte da biblioteca padrão do Python.

Não são necessárias dependências externas.

---

## 🚀 Como executar

### 1. Verifique a instalação do Python

No terminal:

```bash
python --version
```

ou, dependendo do sistema:

```bash
python3 --version
```

### 2. Clone o repositório

```bash
git clone <URL_DO_REPOSITORIO>
```

Entre no diretório:

```bash
cd port-scanner
```

### 3. Execute o programa

Windows:

```bash
python port_scanner.py
```

Linux/macOS:

```bash
python3 port_scanner.py
```

---

## 🖥️ Utilização

Ao executar o programa, será solicitado um endereço IP:

```text
Digite o IP que você deseja escanear:
```

Depois da validação, será apresentado o menu:

```text
1 - Varredura Automática
2 - Varredura Manual
3 - EXIT
```

### Varredura automática

A opção automática utiliza uma lista predefinida de portas associadas a serviços comuns:

| Serviço         | Porta |
| --------------- | ----: |
| FTP-data        |    20 |
| FTP             |    21 |
| SSH             |    22 |
| Telnet          |    23 |
| SMTP            |    25 |
| DNS             |    53 |
| HTTP            |    80 |
| POP3            |   110 |
| IMAP            |   143 |
| HTTPS           |   443 |
| SMB             |   445 |
| SMTP Submission |   587 |
| IMAPS           |   993 |
| POP3S           |   995 |
| MySQL           |  3306 |

Exemplo de resultado:

```text
Testando portas, aguarde...

SSH 22 ...... ABERTA
HTTP 80 ...... ABERTA
HTTPS 443 ...... ABERTA

Total de 3 portas abertas.
Tempo de varredura: 15.02 segundos.
```

### Varredura manual

Na opção manual, o usuário pode informar as portas que deseja testar:

```text
Digite as portas desejadas (separe as portas por vírgula, ex: 20, 22, 80...):
```

Por exemplo:

```text
22,80,443,8080
```

A ferramenta valida se os valores estão dentro do intervalo válido de portas:

```text
1 - 65535
```

---

## 🔌 Como o scanner identifica uma porta aberta?

Para cada porta, o programa cria um socket TCP e tenta estabelecer uma conexão:

```python
soc.connect((ip, porta))
```

Quando a conexão é estabelecida, a função retorna `True` e a porta é considerada aberta.

Quando a conexão não pode ser estabelecida, a função retorna `False`.

É importante entender que:

> Uma porta TCP aberta não significa que o programa conseguiu acessar ou autenticar no serviço que está executando nela.

Por exemplo, uma porta `22` aberta indica que existe algo aceitando conexões TCP naquela porta, possivelmente um servidor SSH. Isso não significa que o scanner tenha conseguido realizar autenticação SSH.

---

## ⏱️ Timeout

Cada tentativa de conexão possui um timeout de:

```text
1 segundo
```

Isso evita que uma porta que não responde faça a varredura permanecer bloqueada indefinidamente.

O uso de timeout também permite praticar um conceito importante no desenvolvimento de aplicações de rede: uma operação de comunicação pode não receber uma resposta dentro do período esperado.

---

## 📁 Estrutura do projeto

Uma estrutura simples para o projeto:

```text
port-scanner/
│
├── port_scanner.py
└── README.md
```

---

## 🎯 Objetivo de aprendizado

Este projeto foi desenvolvido **exclusivamente para estudar e praticar a linguagem Python**.

A ideia é utilizar uma aplicação pequena e concreta para exercitar conceitos que podem ser difíceis de compreender apenas de forma teórica.

Durante o desenvolvimento, foram praticados conceitos como:

```text
Python
  │
  ├── Funções
  ├── Estruturas de dados
  ├── Exceções
  ├── Context managers
  ├── Type hints
  └── Biblioteca padrão
          │
          ▼
       socket
          │
          ▼
        TCP
          │
          ▼
       Portas
```

O projeto também serve como exercício para desenvolver habilidades de organização de código, reutilização de funções, tratamento de entradas e gerenciamento de recursos.

---

## 🔮 Possíveis melhorias futuras

Como exercício de evolução do projeto, algumas funcionalidades podem ser implementadas futuramente:

* Permitir informar intervalos de portas, como `1-1024`.
* Permitir múltiplos hosts.
* Implementar varredura concorrente.
* Melhorar a classificação dos resultados.
* Identificar serviços através de banner grabbing.
* Adicionar suporte a IPv6.
* Exportar resultados para JSON ou CSV.
* Permitir configurar o timeout.
* Adicionar argumentos de linha de comando.
* Criar testes automatizados.
* Melhorar a apresentação dos resultados.

Essas funcionalidades não fazem parte da versão atual para manter o projeto pequeno e focado no estudo dos fundamentos da linguagem Python.

---

## ⚠️ Observação

Este projeto foi desenvolvido **exclusivamente para fins educacionais e para estudo da linguagem Python**.

Ao utilizar a ferramenta em ambientes de rede, faça isso somente em sistemas próprios, ambientes de laboratório ou sistemas para os quais você tenha autorização.






