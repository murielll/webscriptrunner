from django.contrib import admin
from scripts.models import Script


class ScriptAdmin(admin.ModelAdmin):
    list_display = ('name', 'visible')
    list_filter = ('visible',)
    search_fields = ['filename']
    fieldsets = (
        ('Visibility', {
            'fields': ('visible',)
        }),
        ('Script options', {
            'fields': ('filename', 'description', 'args', 'interpreter')
        }),
    )

admin.site.register(Script, ScriptAdmin)
