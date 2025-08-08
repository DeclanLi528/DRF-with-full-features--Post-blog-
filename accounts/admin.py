from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin #继承默认的用户管理界面
from .forms import CustomUserChangeForm, CustomUserCreationForm # 自定义表
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "name",
        "is_staff",
    ]
    # 编辑页的字段分组（在默认分组基础上追加）
    fieldsets = UserAdmin.fieldsets + ((None, {"fields":("name",)}),)
    # 添加用户的字段分组，（在默认分组基础上追加）
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields":("name",)}),)

admin.site.register(CustomUser, CustomUserAdmin)