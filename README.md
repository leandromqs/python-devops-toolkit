# Python DevOps Toolkit

> Um conjunto de ferramentas desenvolvidas em Python para automatizar tarefas comuns do dia a dia de um profissional DevOps.

## 📖 Sobre o projeto

Durante meus estudos em Python, percebi que grande parte dos exercícios disponíveis ensina apenas a sintaxe da linguagem. Embora isso seja importante, poucos projetos simulam problemas encontrados em ambientes de infraestrutura, automação e operações.

Este repositório nasceu com um objetivo simples: aprender Python construindo ferramentas que façam sentido para quem trabalha com DevOps.

Nenhum projeto aqui tem a intenção de substituir soluções consolidadas do mercado, como Docker, Ansible, Prometheus ou Grafana. Pelo contrário, a proposta é utilizá-las como referência e desenvolver pequenas ferramentas que automatizem tarefas repetitivas, integrem serviços ou facilitem atividades do dia a dia.

Cada diretório representa um projeto independente, desenvolvido para praticar conceitos específicos de Python enquanto resolve um problema real.

---

## 🎯 Objetivos

* Praticar Python através de projetos aplicados.
* Desenvolver ferramentas inspiradas em cenários reais de DevOps.
* Explorar automação de tarefas administrativas.
* Aprender a trabalhar com APIs, arquivos, processos, redes e sistemas operacionais.
* Construir um portfólio que demonstre evolução técnica ao longo dos estudos.

---

## 🛠️ Projetos

| Projeto                      | Descrição                                                                   |
|------------------------------| --------------------------------------------------------------------------- |
| **01-auditor-de-servidores** | Cadastro e gerenciamento de servidores utilizando arquivos JSON.            |
| **02-ping-monitor**          | Verificação de disponibilidade de hosts através de ping.                    |
| **03-port-scanner**          | Scanner simples de portas TCP para fins de diagnóstico.                     |
| **04-http-monitor**          | Monitoramento de endpoints HTTP, tempo de resposta e status das aplicações. |
| **05-api-client**            | Cliente para consumo e testes de APIs REST.                                 |
| **06-log-analyzer**          | Leitura e análise de arquivos de log com geração de estatísticas.           |
| **07-file-organizer**        | Organização automática de arquivos e diretórios.                            |
| **08-backup**                | Automatização de backups e compactação de arquivos.                         |
| **09-system-monitor**        | Coleta de informações sobre CPU, memória, disco e utilização do sistema.    |
| **10-docker-manager**        | Automação de tarefas comuns envolvendo containers Docker.                   |
| **11-auto-deploy**           | Automatização de processos de deploy utilizando ferramentas já existentes.  |
| **12-ssl-checker**           | Verificação de certificados SSL/TLS e datas de expiração.                   |
| **13-mini-ansible**          | Execução de comandos em múltiplos servidores via SSH.                       |
| **14-linux-users**           | Automação do gerenciamento de usuários Linux.                               |
| **15-network-inventory**     | Coleta automática de informações de equipamentos e servidores da rede.      |

---

## 📂 Estrutura do repositório

```text
python-devops/
│
├── 01-servidores
├── 02-ping-monitor
├── 03-port-scanner
├── 04-http-monitor
├── 05-api-client
├── 06-log-analyzer
├── 07-file-organizer
├── 08-backup
├── 09-system-monitor
├── 10-docker-manager
├── 11-auto-deploy
├── 12-ssl-checker
├── 13-mini-ansible
├── 14-linux-users
└── 15-network-inventory
```

Cada projeto possui seu próprio **README**, contendo:

* Objetivo da ferramenta
* Problema que ela resolve
* Tecnologias utilizadas
* Como executar
* Exemplos de uso
* Próximas melhorias

---

## 🚀 Tecnologias

Ao longo do desenvolvimento deste repositório serão utilizados, entre outros:

* Python
* Requests
* Paramiko
* Psutil
* Docker SDK
* PyYAML
* Rich
* Click / Typer
* Pandas
* Logging
* JSON
* CSV
* Subprocess
* Socket

---

## 📌 Status

Este é um projeto em desenvolvimento contínuo.

Novas ferramentas serão adicionadas conforme avanço nos estudos e encontro problemas interessantes para automatizar.

---

## 💡 Filosofia do projeto

A proposta deste repositório não é reinventar ferramentas existentes.

Sempre que possível, os projetos buscarão integrar, complementar ou automatizar soluções amplamente utilizadas no ecossistema DevOps.

O foco está em compreender como essas ferramentas funcionam, como interagem entre si e como Python pode ser utilizado para simplificar tarefas operacionais.

---

## 📄 Licença

Este projeto está licenciado sob a licença MIT.
