
# 📝 Task API – Node.js + Fastify + Postgres

Este é um projeto de estudo, focado em aprender **Node.js** com **Fastify** no desenvolvimento de APIs.
A aplicação consiste em uma **API de tarefas** integrada com um banco de dados **Postgres**, hospedado no **Neon**.

## 🚀 Tecnologias utilizadas

* [Node.js](https://nodejs.org/)
* [Fastify](https://fastify.dev/) – framework web
* [Postgres.js](https://github.com/porsager/postgres) – comunicação com o banco
* [Neon](https://neon.tech/) – Postgres serverless em nuvem
* [dotenv](https://www.npmjs.com/package/dotenv) – variáveis de ambiente

---

## ⚙️ Funcionalidades

* **Criar tarefa** (`POST /tasks`)
* **Listar tarefas** (`GET /?search=`) com suporte a filtro por título (**query selector**)
* **Atualizar tarefa** (`PUT /tasks/:id`) via **route parameters**
* **Deletar tarefa** (`DELETE /tasks/:id`)
* Retorno de **HTTP Response Codes** apropriados para cada operação

---

## 📦 Instalação e uso

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/TaskAPI.git
cd TaskAPI
```

Instale as dependências:

```bash
npm install
```

Configure o arquivo `.env` na raiz do projeto com a URL do seu banco **Neon**:

```env
DATABASE_URL="sua_url_do_neon"
```

Crie a tabela no Postgres:

```bash
node create-table.js
```

Execute o servidor em modo desenvolvimento:

```bash
npm run dev
```

A API estará disponível em:
👉 `http://localhost:3333`

---

## 📚 Próximos passos

* Estruturar melhor o projeto com **modularização e organização de pastas**
* Adicionar **Docker + Postgres** para facilitar deploy e ambiente de desenvolvimento
* Explorar autenticação e middlewares

---
