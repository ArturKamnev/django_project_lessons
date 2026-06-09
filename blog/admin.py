from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Fighter)
class FighterAdmin(admin.ModelAdmin):
    exclude = ('views',)
    


admin.site.register(models.FactsMk)