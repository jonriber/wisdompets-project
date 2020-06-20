from django.contrib import admin

from . models import Pet,Vaccine

@admin.register(Pet) #using decorator to register model on admin page
class PetAdmin(admin.ModelAdmin):
    list_display = ['name','species','breed','age','sex']

@admin.register(Vaccine)
class VacAdmin(admin.ModelAdmin):
    list_display = ['name',]