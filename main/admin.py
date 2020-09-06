from django.contrib import admin
from . import models


class ImgTabular(admin.TabularInline):
    model = models.Image
    extra = 1

    
@admin.register(models.SetImage)
class SetImgsAdmin(admin.ModelAdmin):
    inlines = (ImgTabular,)
