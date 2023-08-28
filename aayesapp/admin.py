from django.contrib import admin
from .models import Application


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'approved_by_dc',
                    'approved_by_zc', 'approved_by_sc', 'status']


admin.site.register(Application, ApplicationAdmin)
