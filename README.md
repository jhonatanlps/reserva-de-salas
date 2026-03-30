# Sistema de Reserva de Salas – FIAP

## 📌 Descrição do Projeto

Este projeto tem como objetivo desenvolver um sistema web para gerenciamento de reservas de salas da FIAP, permitindo que estudantes e professores solicitem agendamentos de forma organizada, enquanto a administração possui controle centralizado das solicitações e disponibilidade dos espaços.

O sistema busca substituir o processo atual baseado em e-mails, que apresenta problemas de desorganização, falta de padronização e dificuldade no acompanhamento das reservas. 

---

## 🎯 Objetivo

Criar uma aplicação que permita:

* visualizar salas disponíveis
* solicitar reservas de forma padronizada
* acompanhar o status das solicitações
* manter histórico de agendamentos
* melhorar a comunicação entre usuários e administração

---

## 👥 Integrantes do Grupo

* Vanessa Iris Nobre Ribas – RM 559211
* Kethely Ester da Silva – RM 559187
* Iury Cardoso Araujo – RM 558850
* Bruno Takaya – RM 554986
* Jhonatan Lopes da Silva – RM 559174 

---

## 🚨 Problema Identificado

A instituição apresenta dificuldades no controle e na liberação de acesso às salas e espaços acadêmicos. Atualmente, as solicitações são feitas por e-mail, o que gera:

* falta de organização
* retrabalho
* dificuldade de acompanhamento
* pouca transparência no processo 

---

## 💡 Solução Proposta

Desenvolvimento de um sistema web que permita:

* visualização clara de salas e horários disponíveis
* envio e acompanhamento de solicitações
* cancelamento de reservas
* notificações automáticas por e-mail

Isso torna o processo mais eficiente, transparente e acessível para todos os envolvidos. 

---

## 👤 Personas do Sistema

### 🎓 Estudante – Adelaide

* 20 anos
* Precisa reservar salas para desenvolvimento de projetos e challenges
* Deseja consultar disponibilidade, solicitar reservas e acompanhar status

### 👩‍🏫 Professora – Filomena

* Necessita reservar salas para aulas extras e reposições
* Precisa consultar horários, solicitar com antecedência e visualizar histórico

### 🏢 Administradora – Zuleica

* Responsável por aprovar ou recusar solicitações
* Gerencia disponibilidade e restrições de acesso
* Acompanha o histórico geral de reservas 

---

## 📋 Escopo do Sistema

### Inclui

* Login de usuários
* Solicitação e cancelamento de reservas
* Visualização de disponibilidade
* Acompanhamento de status
* Histórico de reservas
* Notificações por e-mail

### Não inclui (nesta versão)

* Integração com sistemas acadêmicos externos
* Controle de equipamentos das salas
* Pagamentos ou cobranças por reservas 

---

## ⚙️ Requisitos Funcionais

| ID     | Descrição                                    | Prioridade |   |
| ------ | -------------------------------------------- | ---------- | - |
| RF-001 | Login com e-mail institucional               | Alta       |   |
| RF-002 | Visualizar salas disponíveis                 | Alta       |   |
| RF-003 | Solicitar reserva de sala                    | Alta       |   |
| RF-004 | Acompanhar status da solicitação             | Alta       |   |
| RF-005 | Cancelar reserva                             | Média      |   |
| RF-006 | Enviar e-mail de confirmação                 | Alta       |   |
| RF-007 | Enviar e-mail com status (aprovado/recusado) | Alta       |   |
| RF-008 | Enviar e-mail de cancelamento                | Alta       |   |
| RF-009 | Manter histórico de reservas                 | Média      |   |
| RF-010 | Visualizar histórico                         | Média      |   |
| RF-011 | Permitir reservas antecipadas                | Alta       |   |
| RF-012 | Filtrar salas por unidade                    | Média      |   |
| RF-013 | Bloquear áreas para usuários específicos     | Alta       |   |

---

## 🔒 Requisitos Não Funcionais

| ID      | Descrição                                             | Categoria       |   |
| ------- | ----------------------------------------------------- | --------------- | - |
| RNF-001 | Disponibilidade de 99.9%                              | Disponibilidade |   |
| RNF-002 | Interface simples e intuitiva                         | Usabilidade     |   |
| RNF-003 | Suporte a até 200 usuários simultâneos                | Desempenho      |   |
| RNF-004 | Armazenamento seguro de senhas com bcrypt             | Segurança       |   |
| RNF-005 | Criptografia de dados com AES                         | Segurança       |   |
| RNF-006 | Logs armazenados por 5 anos                           | Segurança       |   |
| RNF-007 | Processamento de agendamentos em até 3 segundos       | Desempenho      |   |
| RNF-008 | Bloqueio após 5 tentativas de login inválidas         | Segurança       |   |
| RNF-009 | Encerramento de sessão após 15 minutos de inatividade | Segurança       |   |

---

## 🧭 Atores do Sistema

* **Estudante** – realiza solicitações de reserva
* **Professor** – realiza solicitações de reserva
* **Administrador** – aprova, recusa e gerencia reservas

---

## 🧱 Modelagem do Sistema

O sistema foi modelado utilizando UML, incluindo:

* Diagrama de Casos de Uso
* Diagrama de Atividades

Esses diagramas representam a interação dos usuários com o sistema e o fluxo interno dos processos de reserva.

*(Inserir aqui imagens dos diagramas exportadas do Whimsical ou Miro)*

---

## 🛠️ Tecnologias Utilizadas

*(Preencher quando a implementação for definida)*

Exemplo:

* Frontend: React
* Backend: Node.js
* Banco de Dados: PostgreSQL

---

## 📅 Status do Projeto

Checkpoint 1 – Levantamento de requisitos e modelagem inicial concluídos.

---

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos na disciplina de Engenharia de Software da FIAP.
