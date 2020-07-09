from django.contrib import admin

from project.models.event import Event


class EventAdmin(admin.ModelAdmin):
    readonly_fields = ["slug"]


admin.site.register(Event, EventAdmin)
