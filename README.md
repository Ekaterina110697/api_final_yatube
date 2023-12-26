#  Проект YaTube API
## Описание
Yatube — это платформа для блогеров.Данная платформа дает возможность зарегистрироваться пользователю, создавать, редактировать или удалять собственные посты, а также прокомментировать пост другого автора и подписаться на него.
## Как запустить проект:
Клонируем себе репозиторий:
```
git clone <ваша ссылка на репозиторий>
```
Переходим в директорию:
```
cd api_final_yatube
```
Cоздаем и активируем виртуальное окружение:

Если у вас Linux/MacOS:
```
python3 -m venv venv
source venv/bin/activate
```
Если у вас Windows:
```
python -m venv venv
source venv/Scripts/activate
```
Устанавливаем зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Выполняем миграции:
```
python manage.py migrate
```

Запускаем проект:
```
python manage.py runserver
```
## Примеры запросов к API:
Создание публикации
```
REQUEST:
POST http://127.0.0.1:8000/api/v1/posts/
RESPONSE:
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
Добавление комментария
```
REQUEST:
POST http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
RESPONSE:
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```
