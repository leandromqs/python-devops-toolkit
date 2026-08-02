# Auditor de Servidores v1.0

Uma aplicação desenvolvida em **Python** para gerenciar servidores e seus respectivos endereços IP diretamente pelo terminal.

O projeto foi criado com o objetivo de praticar conceitos fundamentais da linguagem, como manipulação de dicionários, funções, tratamento de exceções, leitura e escrita de arquivos JSON e validação de endereços IP utilizando bibliotecas da própria linguagem.

---

## Funcionalidades

* Listar servidores cadastrados
* Pesquisar servidores pelo nome
* Adicionar novos servidores
* Remover servidores
* Alterar o endereço IP de um servidor
* Salvar os dados em um arquivo JSON
* Carregar servidores a partir de um arquivo JSON

---

## 🛠️ Tecnologias utilizadas

* Python 3
* Biblioteca `json`
* Biblioteca `ipaddress`

---

## 📂 Estrutura dos dados

Os servidores são armazenados em um dicionário no formato:

```python
{
    "servidor_web": "192.168.0.10",
    "servidor_db": "192.168.0.20"
}
```

Ao salvar os dados, o dicionário é convertido para um arquivo JSON com indentação para facilitar a leitura.

---

## ▶️ Como executar

Clone o repositório:

```bash
git clone 
```

Entre na pasta do projeto:

```bash
cd 01-auditor-de-servidores
```

Execute o programa:

```bash
python auditor_de_servidores.py
```

---

## 📚 Conceitos praticados

Este projeto foi desenvolvido para consolidar conhecimentos sobre:

* Funções
* Estruturas de decisão
* Estruturas de repetição
* Dicionários
* Manipulação de arquivos
* Serialização e desserialização de JSON
* Tratamento de exceções (`try` / `except`)
* Validação de dados
* Organização de código

---

## 📄 Licença

Este projeto foi desenvolvido para fins de estudo e prática da linguagem Python.
