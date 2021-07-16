from django.contrib import admin
from .models import student

# Register your models here.
@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display = ['reg_no','name','branch','image']