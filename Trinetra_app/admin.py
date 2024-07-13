from django.contrib import admin
from .models import CareerForm


# Register your models here.

@admin.register(CareerForm)
class CareerFormAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone', 'choose_position', 'year_of_experience',  'address' ,'address2','resume']
