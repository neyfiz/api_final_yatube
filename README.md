# API Final Yatube

API для проекта Yatube — социальной сети для публикации постов. API предоставляет интерфейс для управления публикациями, комментариями и подписками на пользователей.

## Функциональные возможности

С помощью API Yatube можно:
- Работать с постами: создание, изменение, удаление и просмотр постов.
- Комментировать посты: добавление, просмотр и удаление комментариев к постам.
- Подписываться на пользователей: просмотр подписок и добавление новых.

## Технологии

- Python 3.8+
- Django 3.2.16
- Django REST Framework 3.12.4
- JWT-аутентификация: Simple JWT
- SQLite3

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone git@github.com:neyfiz/api_final_yatube.git
    ```
2. Перейдите в каталог проекта:
    ```bash
    cd api_final_yatube
    ```
3. Создайте и активируйте виртуальное окружение:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Linux/Mac
    venv\Scripts\activate  # Для Windows
    ```
4. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```
5. Примените миграции:
    ```bash
    python manage.py migrate
    ```
6. Запустите сервер:
    ```bash
    python manage.py runserver
    ```

Теперь проект доступен по адресу: `http://127.0.0.1:8000/`.

## Запросы

1. **GET** `/api/v1/posts/`

    **Ответ:**
    ```json
    {
      "count": 123,
      "next": "http://api.example.org/posts/?offset=400&limit=100",
      "previous": "http://api.example.org/posts/?offset=200&limit=100",
      "results": [
        {
          "id": 1,
          "title": "Заголовок поста",
          "content": "Содержимое поста",
          "author": "username",
          "created_at": "2024-01-01T12:00:00Z",
          "updated_at": "2024-01-01T12:00:00Z"
        }
      ]
    }
    ```

3. **POST** `/api/v1/posts/`

    **Запрос:**
    ```json
    {
      "title": "Заголовок поста",
      "content": "Содержимое поста"
    }
    ```
    **Ответ:**
    ```json
    {
      "id": 1,
      "title": "Заголовок поста",
      "content": "Содержимое поста",
      "author": "username",
      "created_at": "2024-01-01T12:00:00Z"
    }
    ```
Проект разработан [neyfiz.](https://github.com/neyfiz)
