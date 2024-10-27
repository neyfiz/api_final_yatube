# API Final Yatube

API для проекта Yatube — социальной сети для публикации постов. С помощью этого API можно:

- Создавать, изменять и удалять посты.
- Оставлять комментарии к постам.
- Подписываться на других пользователей.

## Установка

1. Клонируйте репозиторий:
    ```bash
   git clone git@github.com:neyfiz/api_final_yatube.git
3. Перейдите в каталог проекта:
    ```bash
    cd api_final_yatube
3. Создайте и активируйте виртуальное окружение:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Linux/Mac
    venv\Scripts\activate  # Для Windows
4. Установите зависимости:
    ```bash
    pip install -r requirements.txt
5. Примените миграции:
    ```bash
    python manage.py migrate
6. Запустите сервер:
    ```bash
    python manage.py runserver
