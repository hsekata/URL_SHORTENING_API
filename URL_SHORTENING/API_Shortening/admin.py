from django.contrib import admin
from .models import URL
# Register your models here.
class URLAdmin(admin.ModelAdmin):
    list_display = ('url', 'shortcode', 'createdAt', 'updatedAt')
admin.site.register(URL)