from django.contrib import admin
from .models import User,Student


class UserAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email','password')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','f_name','l_name','email','phone','password')



# Register your models here.
admin.site.register(User,UserAdmin)
admin.site.register(Student,StudentAdmin)