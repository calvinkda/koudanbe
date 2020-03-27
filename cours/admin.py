from django.contrib import admin
from cours.models import Courses, Classes


class CoursesModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    prepopulated_fields = {
        'slug': ('title',)
    }

admin.site.register(Courses, CoursesModelAdmin)
admin.site.register(Classes)