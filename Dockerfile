FROM python:3.12.0-bullseye

WORKDIR /nginx_log_parser

COPY . /nginx_log_parser

# Установите зависимости
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Выполните миграции и соберите статику
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
