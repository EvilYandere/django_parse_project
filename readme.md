# Django Parse
## Описание проекта
Парсинг логов по шаблону, загрузка данных в БД, вывод результатов в админку и API (DRF)
## Запуск проекта
### Через Docker
1. Запустить Docker Desktop
2. Выполнить команду `docker compose up --build`
3. Внутри контейнера выполнить `docker-compose exec web python manage.py import_log <путь до файла>`
4. Результаты будут доступны по адресу http://localhost:8000
### Без использования Docker
1. Выполнить команду `python manage.py runserver`
2. Выполнить команду `python manage.py import_log <путь до файла>`
3. Результаты будут доступны по адресу http://127.0.0.1:8000/

