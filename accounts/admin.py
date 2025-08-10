from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin #继承默认的用户管理界面
from .forms import CustomUserChangeForm, CustomUserCreationForm # 自定义表
from .models import CustomUser

def filter_fieldsets(model, fieldsets):
    model_fields = {f.name for f in model._meta.get_fields()}
    # 把表单字段里的password1/2手动加入
    allowed_extra_fields = {"password1", "password2"}

    new_fieldsets = []
    #python允许在遍历list/tuple的时候直接对元素进行unpacking
    for group_name, group_opts in fieldsets:
        # 这里的fieldsets是UserAdmin.fieldsets
        opts = group_opts.copy()

        if "fields" in opts:
            filtered_fields = tuple(f for f in opts["fields"] if f in model_fields
                                    or f in allowed_extra_fields)
            opts["fields"] = filtered_fields
        
        new_fieldsets.append((group_name, opts))
    return tuple(new_fieldsets)

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
    # # # 编辑页的字段分组（在默认分组基础上追加）
    # fieldsets = UserAdmin.fieldsets + ((None, {"fields":("name",)}),)
    fieldsets = filter_fieldsets(CustomUser, UserAdmin.fieldsets) + \
        ((None, {"fields":("name",)}),)
    # # # 添加用户的字段分组，（在默认分组基础上追加）
    # add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields":("name",)}),)
    add_fieldsets = filter_fieldsets(CustomUser, UserAdmin.add_fieldsets) + \
        ((None, {"fields":("name",)}),)
admin.site.register(CustomUser, CustomUserAdmin)