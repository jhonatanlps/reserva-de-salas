# Sistema de Reserva de Salas - FIAP

## Visão geral

Este projeto é uma aplicação em linha de comando para gerenciamento de reservas de salas da FIAP. O sistema permite cadastro de usuários, autenticação com senha criptografada, solicitação de reservas, aprovação ou recusa por administrador, cancelamento e manutenção do histórico em arquivo JSON.

O objetivo é centralizar o fluxo que antes era feito manualmente, oferecendo mais organização no controle de salas, horários e permissões de acesso.

## Funcionalidades atuais

* cadastro de usuários com nível de acesso
* login com validação de senha usando bcrypt
* busca de salas por unidade, data e horário
* criação de solicitações de reserva
* aprovação ou negação de solicitações pelo administrador
* criação automática de reservas aprovadas
* cancelamento de reservas por usuário ou administrador
* restrição de acesso por sala, com níveis de permissão
* persistência dos dados em `data/database.json`

## Perfis de acesso

* `1 - Professor`: pode buscar salas e cancelar suas reservas
* `2 - Aluno`: pode buscar salas e cancelar suas reservas
* `3 - Administrador`: pode analisar solicitações, aprovar ou negar reservas, cancelar reservas e restringir acesso às salas

## Requisitos do projeto

* Python 3.x
* Dependência principal: `bcrypt`

Instalação:

```bash
pip install -r requirements.txt
```

## Como executar

```bash
python main.py
```

Ao iniciar, o sistema carrega os dados de `data/database.json` e, ao encerrar, salva as alterações no mesmo arquivo.

## Estrutura do projeto

```text
main.py
auth/
	login.py
	signin.py
data/
	database.json
models/
	reserva.py
	solicitacao.py
	usuario.py
repositories/
	db.py
services/
	admin.py
	reserva_salas.py
views/
	login_window.py
	main_window.py
```

## Como funciona o fluxo

1. O usuário informa se já possui conta.
2. Se necessário, realiza o cadastro.
3. Após o login, o sistema exibe o menu conforme o nível do usuário.
4. O usuário consulta unidades, salas, datas e horários disponíveis.
5. A solicitação é registrada como pendente.
6. O administrador aprova ou nega a solicitação.
7. As reservas e solicitações são salvas no JSON ao final da execução.

## Dados iniciais

O arquivo `data/database.json` contém a base inicial do sistema, incluindo:

* usuários cadastrados
* unidades e salas disponíveis
* datas e horários configurados
* solicitações pendentes
* reservas já registradas

## Integrantes do grupo

* Vanessa Iris Nobre Ribas - RM 559211
* Kethely Ester da Silva - RM 559187
* Iury Cardoso Araujo - RM 558850
* Bruno Takaya - RM 554986
* Jhonatan Lopes da Silva - RM 559174

## Demonstração

Vídeo de teste do sistema: https://youtu.be/0D8d75-WakY
