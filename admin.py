from django.contrib import admin
from canvas.models import Canvas, Item

class CanvasAdmin(admin.ModelAdmin):
    fields =  ['name']

admin.site.register(Canvas)
admin.site.register(Item)
