from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .forms import UserCreationForm, UserChangeForm
from .models import User


class UserAdmin(BaseUserAdmin): # UserAdmin class is responsible for how the show information in Admin Panel
    # Override(mandatory)
    
    # use two form
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('__str__', 'email', 'phone', 'is_admin')
    list_filter = ('is_admin',)

    # first form
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'phone', 'password')}),
        ('Personal Info', {'fields': ('is_active',)}),
        ('Permissions', {'fields': ('is_admin',)})
    )
    # second form
    add_fieldsets = (
        (None, {'fields': ('email', 'phone', 'password', 'password_confirm')}),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)