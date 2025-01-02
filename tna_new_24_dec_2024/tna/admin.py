from django.contrib import admin
from .models import Task, Notification

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    pass

# Register your models here.
