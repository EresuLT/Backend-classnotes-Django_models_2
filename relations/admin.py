from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Creator)
admin.site.register(Language)
admin.site.register(Framework)
admin.site.register(Developer)
