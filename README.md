# 📖 Manuscripts API

**Manuscripts API** — это простое FastAPI-приложение для работы с рукописями (истории, новеллы, тексты).  
Позволяет добавлять новые рукописи и получать список всех сохранённых произведений.

---

## Технологии

- [Python 3.11+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/) — фреймворк для API
- [SQLAlchemy](https://docs.sqlalchemy.org/) — ORM для работы с базой данных
- [Pydantic](https://docs.pydantic.dev/) — валидация данных
- [SQLite + aiosqlite](https://docs.python.org/3/library/sqlite3.html) — база данных

---

## Установка и запуск

1. Клонируй репозиторий:

   ```bash
   git clone https://github.com/Anissa667u/manuscripts-api.git
   cd manuscripts-api

   ```

2. Создай виртуальное окружение
   python -m venv venv (Если не получается: py -m venv venv)
   source venv/bin/activate # Linux/Mac
   ./venv/Scripts/Activate.ps1 # Windows

3. Установи зависимости
   pip install -r requirements.txt (список нужных библиотек в requirements.txt)

4. Запусти сервер
   uvicorn main:app --reload

## Сервер будет доступен по адресу:

👉 http://127.0.0.1:8000

## Документация API:

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc

📌 **Эндпоинты**
POST /setup_database
Инициализация базы данных (создание таблиц).

POST /manuscripts
Добавить новую рукопись.

Пример тела запроса:
{
"title": "Моя первая рукопись",
"author": "Анисса А",
"description": "История о том, как идеи превращаются в слова..."
}

GET /manuscripts
Получить список всех рукописей.
Ответ(пример):
[
{
"id": 1,
"title": "Моя первая рукопись",
"author": "Анисса А",
"description": "История о том, как идеи превращаются в слова..."
}
]

## Структура проекта:

manuscripts-api/
├── main.py # Основное приложение FastAPI
├── manuscripts.db # SQLite база данных
├── requirements.txt # Зависимости проекта
├── README.md # Документация проекта
└── venv/ # Виртуальное окружение (локально)

## 🔮 Планы по доработке

- Добавить больше эндпоинтов и связать несколько таблиц в БД, чтобы API выглядело как полноценный бэкенд приложения
- Разделить код на модули (`models.py`, `schemas.py`, `routes/`) для лучшей архитектуры и читаемости
- Написать автотесты на `pytest` для проверки стабильности и корректности работы

## 👩‍💻 Автор

Проект создан с любовью 💜 by Anissa
