import json
from datetime import datetime
from django.core.management.base import BaseCommand
from logs.models import LogEntry


class Command(BaseCommand):
    help = 'Import log file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the log file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        with open(file_path, 'r') as file:  # файл с логами открывается на чтение
            for line in file:  # считывается построчно
                try:
                    data = json.loads(line)
                    log_date = datetime.strptime(data['time'], '%d/%b/%Y:%H:%M:%S %z')
                    LogEntry.objects.create(  # выполняется поиск полей из модели
                        ip_address=data['remote_ip'],
                        log_date=log_date,
                        http_method=data['request'].split()[0],
                        uri=data['request'].split()[1],
                        status_code=int(data['response']),
                        response_size=int(data['bytes'])
                    )
                except json.JSONDecodeError as e:  # обработка ошибок
                    print(f"JSON decode error: {e}")
                except Exception as e:
                    print(f"Error creating LogEntry: {e}")

        self.stdout.write(self.style.SUCCESS('Log file imported successfully'))  # сообщение об успешном
        # О считывании файла
