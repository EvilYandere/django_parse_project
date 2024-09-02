from django.db import models


class LogEntry(models.Model):   # описание модели через ORM
    ip_address = models.GenericIPAddressField()
    log_date = models.DateTimeField()
    http_method = models.CharField(max_length=10)
    uri = models.TextField()
    status_code = models.IntegerField()
    response_size = models.BigIntegerField()

    def __str__(self):
        return f"{self.ip_address} - {self.http_method} {self.uri}"
