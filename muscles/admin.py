from django.contrib import admin
from .models import MuscleGroup, Muscle


class MuscleGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'ar_name',  'body_part')


class MuscleAdmin(admin.ModelAdmin):
    list_display = ('name', 'ar_name', 'muscle_group')


admin.site.register(Muscle, MuscleAdmin)
admin.site.register(MuscleGroup, MuscleGroupAdmin)

