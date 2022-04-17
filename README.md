# yamdb_final
![yamdb_workflow](https://github.com/kostkh/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

API для учебного проекта YaMDB - учебного проекта соц.сети, в котором пользователи могут размещать обзоры на произведения в разных категориях (фильмы, музыка, кино) и жанрах, после чего на основании оценок формируется рейтинг произведений. 

API позволяет: 
- зарегистрировать пользователя;
- управлять списком категорий, жанров, произведений;
- получать, размещать изменять и удалять отзывы, комментарии к ним;

В проекте:
- реализован REST API CRUD для основных моделей проекта; 
- для аутентификации используется токен Simple-JWT;
- настроено разграничение прав доступа к эндпойнтам API для разных групп пользователей;
- реализованы фильтрации, сортировки;
- реализован поиск по жанрам, категориям, именам пользователей;
- настроена пагинация ответов от API.

## Системные требования
- Python 3.7+
- Works on Linux, Windows, macOS

## Технологии:
- Python 3.7
- Django 2.2.6
- Django REST Framework
- Simple-JWT
- Postgres

## Как запустить проект:

- Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/KostKH/yamdb_final.git
cd yamdb_final
```
- Проверить, что свободны порты, необходимые для работы приложения: порт 8000 (требуется для работы приложения) и порт 5432 (требуется для работы  Postgres)

- Cоздать и открыть файл .env с переменными окружения:
```
cd infra
touch .env
```
- Заполнить .env файл с переменными окружения (SECR_KEY см. в файле settings.py - константа SECRET_KEY). Пример:
```
echo SECR_KEY=************ >>.env
echo DB_ENGINE=django.db.backends.postgresql >>.env
echo DB_NAME=postgres >>.env
echo POSTGRES_PASSWORD=postgres >>.env
echo POSTGRES_USER=postgres >>.env
echo DB_HOST=db >>.env
echo DB_PORT=5432 >>.env
```
- Установить и запустить приложения в контейнерах:
```
docker-compose up -d
```
- Запустить миграции, создать суперюзера, собрать статику и заполнить БД:
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```

## Документация по API
Документация доступна по эндпойнту /redoc/

## Примеры

#### Авторизация пользователей:
```
/api/v1/auth/signup/ - регистрация пользователя (POST)
/api/v1/auth/token/ - ввод полученного токена (POST)
```
#### Работа с категориями, жанрами:
```
/api/v1/categories/ - просмотр (GET), создание (POST) категорий 
/api/v1/categories/{slug}/ - удаление категории (DELETE)
/api/v1/genres/ - просмотр (GET), создание (POST) жанров
/api/v1/genres/{slug}/ - удаление категории (DELETE)
/api/v1/titles/ - просмотр (GET), создание (POST) записи о произведении
/api/v1/titles/{titles_id}/ - управление произведением (GET, PATCH, DELETE)
```
#### Работа с обзорами и комментариями:
```
/api/v1/titles/{title_id}/reviews/ - просмотр (GET), создание (POST) обзоров
/api/v1/titles/{title_id}/reviews/{review_id}/  - управление обзором (GET, PATCH, DELETE)
/api/v1/titles/{title_id}/reviews/{review_id}/comments/ - просмотр (GET), создание (POST) комментариев
/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/  - управление комментарием (GET, PATCH, DELETE)
```
#### Работа с базой пользователей:
```
/api/v1/users/ - просмотр (GET), создание (POST) пользователей
/api/v1/users/{username}/ - управление пользователем (GET, PATCH, DELETE)
/api/v1/users/me/ - просмотр или изменение пользователем своих данных  (GET, PATCH)
```
## О программе:

Лицензия: BSD 3-Clause License

Автор: Константин Харьков