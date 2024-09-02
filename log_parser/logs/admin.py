from django.contrib import admin
from .models import LogEntry


@admin.register(LogEntry)   # регистрация модели (и ее полей)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'log_date', 'http_method', 'uri', 'status_code', 'response_size')
    search_fields = ('ip_address', 'uri')
    list_filter = ('http_method', 'status_code')
