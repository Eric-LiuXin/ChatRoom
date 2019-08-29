from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # 显示的列
    list_display = ['username','ad_full_name', 'email', 'is_staff', 'is_active']

    list_editable = ['is_staff', 'is_active']

    fieldsets = (
        (None, {
            'fields': ('username', 'password', ),
        }),
        ("基础信息",{
            'fields':('first_name', 'last_name', 'email', 'position','type',),
        }),
        ("认证授权",{
            'fields':('is_superuser', 'is_staff', 'is_active', 'user_permissions', 'groups'),
        }),
        ("时间轴", {
            'fields':('date_joined', 'last_login'),
        }),
    )

    readonly_fields = ('date_joined', 'last_login')

    def ad_full_name(self, obj):
        return ("%s%s" % (obj.last_name, obj.first_name)).upper()

    ad_full_name.short_description = '用户姓名'