from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Posts)
admin.site.register(Categories)
admin.site.register(Comments)
# admin.site.register(Users)
admin.site.register(Rating)
