from django.contrib import admin
from .models import Building, Resident


class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'resident_manager', 'added_by', 'modified_by', 'added_on', 'modified_on')
    exclude = ('added_by', 'modified_by')

    def save_model(self, request, obj, form, change):
        if change:
            obj.modified_by = request.user
        else:
            obj.modified_by = request.user
            obj.added_by = request.user
        obj.save()
        super().save_model(request, obj, form, change)

admin.site.register(Building, BuildingAdmin)

class ResidentAdmin(admin.ModelAdmin):
    list_display = ('name', 'rent_amount', 'token_amount',  'location', 'move_in_date', 'move_out_date', 'added_by', 'modified_by')
    exclude = ('added_by', 'modified_by')

    def save_model(self, request, obj, form, change):
        if change:
            obj.modified_by = request.user
        else:
            obj.modified_by = request.user
            obj.added_by = request.user
        obj.save()
        super().save_model(request, obj, form, change)


admin.site.register(Resident, ResidentAdmin)

