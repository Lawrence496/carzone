from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="50" style="border-radius:5px" />'.format(object.car_photo.url))

    thumbnail.short_description = 'car_photo'

    list_display = (
        'id',
        'thumbnail',
        'car_title',
        'year',
        'model',
        'color',
        'state',
        'is_featured',
        'created_on'
    )
    list_display_links = ('car_title','id')
    search_fields = (        
        'car_title',
        'year',
        'model',
        'color',
        'state',)

    list_editable = ('is_featured',)
admin.site.register(Car, CarAdmin)
