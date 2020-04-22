from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from api.models import Ingredient, Tag, User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    ordering = ('id',)
    list_display = ('id', 'email', 'name', 'is_staff', 'is_superuser',)
    search_fields = ('email', 'name')
    fieldsets = (
        (None, {
            'fields': ('email', 'password'),
        }),
        ('Personal Info', {'fields': ('name',)}),
        (
            'Permissions',
            {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups',)}
        ),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'name', 'is_staff', 'groups',),
        }),
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'user',)
    search_fields = ('name',)
    list_editable = ('name',)
    list_display_links = ('user',)
    list_filter = ('name',)


admin.site.register(Ingredient)
