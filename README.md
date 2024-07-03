# Users manager


## Реализованные функции

 - Просмотр зарегистрированных пользователей
 - Просмотр страницы конкретного пользователя
 - Редактирование личного профиля
 - Сброс пароля с восстановлением через почту
 - Идентификаторы пользователей в формате UUID4
 - Доступна админ панель http://localhost/admin/

## Запуск из образа Docker Compose
##### Шаг 1. Клонирование репозитория
Склонируйте репозиторий на локальную машину:
```bash
git clone git@github.com:ZubovEvgeniy/users_manager.git
```
##### Шаг 2. Заполнить файл переменных окружения
В корне проекта создайте файл ".env" по образцу ".env.example"

##### Шаг 3.  Запуск контейнеров
Из корня проекта запустите команду
```bash
docker-compose up -d --build 
```
##### Шаг 4.  Установка миграций, создание супер пользователя, сбор статики, запуск тестов
Последовательно запустите следующие команды:
```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```


## Технологии
* Python 3.9
* Django 4.2.13
* PostgreSQL
* Docker


**Автор**

Евгений Зубов

2024
