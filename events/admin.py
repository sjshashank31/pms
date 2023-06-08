from django.contrib import admin
from .models import Event

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'description', 'location')
    exclude = ('added_by', 'modified_by')

    def save_model(self, request, obj, form, change):
        if change:
            obj.modified_by = request.user
        else:
            obj.modified_by = request.user
            obj.added_by = request.user
        obj.save()
        super().save_model(request, obj, form, change)

admin.site.register(Event, EventAdmin)