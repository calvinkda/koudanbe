from django.contrib import admin
from accounts.models import Learner
# Register your models here.


class LearnerModelAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'serial_number')

admin.site.register(Learner, LearnerModelAdmin)