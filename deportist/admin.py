from django.contrib import admin
from .models import Deportist

@admin.register(Deportist)
class DeportistAdmin(admin.ModelAdmin):
    ordering = ('code',)
    list_display = ('code','name', 'lastname')
