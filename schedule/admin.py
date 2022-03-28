
from django.contrib import admin

from .models import Option, Schedule

admin.site.register(Schedule)
admin.site.register(Option)

