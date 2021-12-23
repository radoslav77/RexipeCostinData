from django.contrib import admin

from .models import *

# Register your models here.


class Import_DataAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "company")


admin.site.register(Import_Data, Import_DataAdmin)


class ExeldocumentAdmin(admin.ModelAdmin):
    list_display = ("doc",)


admin.site.register(Exeldocument, ExeldocumentAdmin)
