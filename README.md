# Сервис аутентификации

Этот проект представляет собой веб-сервис с функциональностью регистрации и входа пользователей. Он состоит из фронтенд-части, написанной на Quasar, бэкенд-части на FastAPI и базы данных PostgreSQL.

## Структура проекта

- `frontend/` - Фронтенд на Quasar
- `backend/` - Бэкенд на FastAPI
- `docker-compose.yml` - Конфигурация Docker Compose

## Требования

- Docker и Docker Compose
- Node.js и npm
- Python 3.7+

## Установка и запуск

### База данных

1. Запустите PostgreSQL с помощью Docker Compose

```bash
docker-compose up -d
```

### Бэкенд

1. Перейдите в директорию backend:
```bash
cd backend
```

2. Создайте и активируйте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate # Для Unix
venv\Scripts\activate # Для Window)))
```

4. Установите зависимости:
```bash
pip install -r requirements.txt
```

6. Примените миграции:
```bash
alembic upgrade head
```

7. Запустите сервер:
```bash
uvicorn main.app:app --reload)))
```

### Фронтенд

1. Перейдите в директорию frontend:

```bash
cd frontend
```

2. Установите зависимости:

```bash
npm install
```


3. Запустите приложение в режиме разработки:
```bash
quasar dev
```

## Использование

После запуска всех компонентов, вы можете открыть веб-браузер и перейти по адресу `http://localhost:8080` (или другому порту, указанному Quasar) для доступа к пользовательскому интерфейсу. Здесь вы сможете зарегистрироваться и войти в систему.

