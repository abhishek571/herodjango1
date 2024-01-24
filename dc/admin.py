from django.contrib import admin
from.models import DC
# Register your models here.
@admin.register(DC)
class DCadmin(admin.ModelAdmin):
    list_display=['id','name','heroicname']