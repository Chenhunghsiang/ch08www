from django.contrib import admin

# Register your models here.
from mysite import models

class PostAdmin(admin.ModelAdmin):
    list_display=('nickname', 'messsage','enabled', 'pub_time')
    ordering=('-pub_time',)
admin.site.register(models.Mood)
# admin.site.register(models.Post, PostAdmin)