# Electronic store chain 🖥🔌📲


[![Python Version](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Django Version](https://img.shields.io/badge/Django-5.0-green.svg)](https://www.djangoproject.com/)
[![DRF Version](https://img.shields.io/badge/DRF-3.15-524E20.svg)](https://www.djangoproject.com/)
[![Djoser Version](https://img.shields.io/badge/Djoser-2.2-777E20.svg)](https://www.djangoproject.com/)
[![DRF YASG Version](https://img.shields.io/badge/DRF_YASG-1.21-333E20.svg)](https://www.djangoproject.com/)
[![PostgreSQL Version](https://img.shields.io/badge/PostgreSQL-16.0-088E20.svg)](https://www.postgresql.org/)
[![Docker Version](https://img.shields.io/badge/Docker-26.0-942E20.svg)](https://www.docker.com/)
[![Docker Compose Version](https://img.shields.io/badge/Docker_Compose-2.26-521E20.svg)](https://www.docker.com/)

***ELECTRONIC STORE CHAIN*** - это онлайн платформа торговой сети электроники.

## 🔍 Backend

Backend часть проекта предполагает реализацию следующего функционала:

- 🔐 Авторизация и аутентификация пользователей
- 👤 Распределение ролей между пользователями (пользователь и админ)
- 📟 CRUD для продуктов
- 🚛 CRUD для поставщиков
- 📒 Для автоматической генерации документации подключен Swagger и Redoc


## 🚀 Установка и запуск

1. Клонировать проект:

```bash
git clone git@github.com:ZuAlVi/electronics_store_chain.git
```

2. Установить зависимости:

```bash
pip install -r requirements.txt
```

3. Создать файл `.env` в корне проекта и внести необходимые данные, взяв за пример файл `.env.example`.

4. Создать базу данных. 

5. Провести миграции:

```bash
python3 manage.py migrate
```
6. Запустить локальный сервер:
```bash
python3 manage.py runserver
```

## 🐳 Запуск через Docker и Docker Compose

1. Docker:
    
- Создаем контейнер:

```bash
docker build -t app-name .
 ```

- Запускаем:

```bash
docker run -p 8000:8000 app-name
 ```

2. Docker Compose:

- Собираем и запускаем контейнер в фоновом режиме одной командой:

```bash
docker-compose up --build
 ```


## 🧟‍♂️👮‍♂️ Тестовые пользователь и админ

1. Создать админа:

```bash
python3 manage.py create_admin
```

- email: admin@admin.ru
- password: admin

2. Создать пользователя:

```bash
python3 manage.py create_user
```

- email: user@user.ru
- password: user
