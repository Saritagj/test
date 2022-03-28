from django.contrib import admin
from .models import UserModel
# Register your models here.

admin.site.site_header = "Django CRUD App"
admin.site.site_title = "Django CRUD App Admin Portal"
admin.site.index_title = "Welcome to Django CRUD App"


@admin.register(UserModel)
class UserDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'gender', 'date_created']

# admin.site.register(UserModel)
