from django.contrib import admin

from .models import *

# Register your models here.


class Import_DataAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "unit", "unit_type", "price", "company")


admin.site.register(Import_Data, Import_DataAdmin)


class ExeldocumentAdmin(admin.ModelAdmin):
    list_display = ("title", "doc")


admin.site.register(Exeldocument, ExeldocumentAdmin)


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'recipe', 'method')


admin.site.register(Recipe, RecipeAdmin)
