from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from account.models import User


class UserAdmin(BaseUserAdmin):

  

    list_display = ('email', 'is_admin','last_login','joined_date')
    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields': ('username','email', 'password')}),
        ('Personal info', {'fields': ('first_name',
                                      'last_name', 'date_of_birth', 'gender')}),
        ('Permissions', {'fields': ('admin', 'staff', 'active')}
            ),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'gender', 'date_of_birth', 'password1', 'password2')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)