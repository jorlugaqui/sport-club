from django.contrib import admin
from .models import Sport, Club, Period, Facility, Coach


@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    ordering = ('name',)


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    ordering = ('name', 'director')
    list_display = ('name', 'director')

@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    ordering = ('name', 'start_date', 'end_date')
    list_display = ('name', 'start_date', 'end_date')

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('name','availability')

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('name','phonenumber')