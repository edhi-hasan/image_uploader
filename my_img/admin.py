from django.contrib import admin
from . models import up_img

# Register your models here.
@admin.register(up_img)
class imgUp(admin.ModelAdmin):
    list_display = ['id','Image','date']