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

## Diferencial
	###Descrição
	Este projeto implementa uma camada robusta de proteção de dados através da biblioteca bcrypt do Python, garantindo que as senhas dos usuários nunca sejam armazenadas em formato de texto simples. O processo consiste em transformar a senha original em um hash criptográfico irreversível, utilizando um algoritmo que gera automaticamente um "salt" (um valor aleatório exclusivo para cada registro), o que assegura que, mesmo que dois usuários possuam senhas idênticas, seus hashes armazenados no banco de dados sejam completamente diferentes.

	###Justificativa
	A escolha do bcrypt é fundamental para a segurança moderna, pois ele foi desenhado para ser computacionalmente "lento" através de um fator de custo ajustável, o que inviabiliza ataques de força bruta em larga escala e protege o sistema contra o uso de Rainbow Tables (tabelas de hashes pré-computados). Em um cenário de vazamento de dados, essa técnica protege a integridade das contas dos usuários, demonstrando conformidade com as melhores práticas de cibersegurança e legislações de privacidade, como a LGPD, ao tratar informações sensíveis com o devido rigor técnico.

	###Referencias
	https://www-geeksforgeeks-org.translate.goog/python/how-to-hash-passwords-in-python/?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc&_x_tr_hist=true
	https://medium.com/py-bcrypt/encriptando-senhas-em-python-com-bcrypt-25e46b5c8166
	https://pypi.org/project/bcrypt/

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
