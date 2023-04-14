from django.contrib import admin
from . models import places
from . models import members

# Register your models here.
admin.site.register(places)

admin.site.register(members)