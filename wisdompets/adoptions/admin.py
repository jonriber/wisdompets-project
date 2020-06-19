from django.contrib import admin

from . models import Pet

@admin.register(Pet) #using decorator to register model on admin page
class PedAdmin(admin.ModelAdmin):
    list_display = ['name','species','breed','age','sex']