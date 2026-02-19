<img width="1919" height="886" alt="Captura de tela 2026-02-18 232731" src="https://github.com/user-attachments/assets/0e1c73f8-414d-4b12-97da-9d20c08dd62f" />

---

# 🧠 Memory Fast API

API REST para treino de memória.
Permite gerar uma sequência com tamanho personalizado e validar a resposta fornecida pelo usuário.

---

## ⚙️ Stack

* Python
* FastAPI
* SQLAlchemy 
* Pydantic
* Uvicorn
* SQLite

---

## 🏗 Arquitetura

Separação em camadas:

```
app/
 ├── core/        # Configuração de banco e dependências
 ├── models/      # Modelos ORM e Schemas Pydantic
 ├── routers/     # Camada HTTP
 ├── services/    # Regras de negócio
 └── main.py      # Inicialização da aplicação

Router → Service → Model → Database
```

---

## 📦 Instalação

Crie o ambiente virtual:

```bash
python -m venv .venv
```

Ative:

Windows:

```bash
.venv\Scripts\activate
```

Linux/Mac:

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

---

## ▶️ Executando a API

Em um terminal:

```bash
uvicorn app.main:app --reload
```

API disponível em:

```
http://127.0.0.1:8000
```

Documentação automática:

```
http://127.0.0.1:8000/docs
```

---

## 🌐 Executando o Frontend

Em outro terminal, vá até a pasta templates e execute:

```bash
python -m http.server 5500
```

Acesse:

```
http://127.0.0.1:5500
```

⚠️ Importante: o backend deve estar rodando simultaneamente em outro terminal.

---

## 📌 Endpoints

Criar treino:

```
POST /training/
```

Buscar treino:

```
GET /training/{id}
```

Responder treino:

```
POST /training/{id}/answer
```

## 🧠 Considerações finais

Ainda pretendo evoluir bastante esta API adicionando autenticação JWT, mais categorias como: palavras, constantes matemáticas, cartas, datas, e até estatísticas pessoais 
para cada usuário de erros e acertos.
