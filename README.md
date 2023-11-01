# Cadastro de Alunos

Este é um programa de cadastro de alunos desenvolvido em Python usando a biblioteca Tkinter e MongoDB para armazenamento de dados. O programa permite que você insira informações sobre alunos, como nome, sobrenome, curso e turno, e salve esses dados em um banco de dados MongoDB local.

## Requisitos

- Python 3.x
- Biblioteca Tkinter
- Biblioteca pymongo
- MongoDB

Certifique-se de ter um servidor MongoDB em execução localmente em `mongodb://127.0.0.1:27017/` para que o programa funcione corretamente.

## Como Usar

1. **Preencha os Detalhes do Aluno**:
   - Insira o nome, sobrenome, curso e turno do aluno nos campos apropriados.

2. **Clique em "Cadastrar"**:
   - Após preencher os detalhes do aluno, clique no botão "Cadastrar" para salvar as informações no banco de dados MongoDB.

3. **Confirmação de Cadastro**:
   - Após o cadastro bem-sucedido, uma mensagem de confirmação será exibida na tela.

## Estrutura do Banco de Dados

O programa utiliza um banco de dados MongoDB chamado `dbapp` e uma coleção chamada `students` para armazenar os dados dos alunos. Cada documento na coleção possui os seguintes campos:
- `nome`: Nome do aluno (com a primeira letra em maiúscula).
- `sobrenome`: Sobrenome do aluno (com a primeira letra em maiúscula).
- `curso`: Curso do aluno (com a primeira letra em maiúscula).
- `turno`: Turno do aluno (com a primeira letra em maiúscula).
- `data_matricula`: Data de matrícula do aluno no formato "dia-mês-ano".

## Interface Gráfica

O programa possui uma interface gráfica simples com campos de entrada para cada detalhe do aluno e um botão "Cadastrar" para realizar o cadastro. Após o cadastro, uma mensagem de confirmação será exibida na tela.

---

**Nota**: Certifique-se de ter uma conexão à internet ativa ao executar o programa para acessar o banco de dados MongoDB. Certifique-se também de que o MongoDB esteja em execução localmente para armazenar os dados do aluno.

Para mais detalhes sobre a biblioteca Tkinter, consulte a [documentação oficial](https://docs.python.org/3/library/tk.html). Para mais informações sobre o pymongo e MongoDB, consulte a [documentação do pymongo](https://pymongo.readthedocs.io/en/stable/) e [MongoDB](https://www.mongodb.com/).

