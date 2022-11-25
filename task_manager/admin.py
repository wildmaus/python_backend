from django.contrib import admin

from .models import Task, StatusChangeHistory

admin.site.register(Task)
admin.site.register(StatusChangeHistory)
