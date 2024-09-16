from django.contrib import admin
from .models import Task
# Register your models here.

# para poder ver los campos de solo lectura
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


# ademas de la clase, se debe registrar la clase admin para poder ver los campos de solo lectura
admin.site.register(Task, TaskAdmin)

