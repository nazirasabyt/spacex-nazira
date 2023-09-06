from django.contrib import admin

# Register your models here.
from .models import Link
from .models import Advantage

admin.site.register(Link)
admin.site.register(Advantage)