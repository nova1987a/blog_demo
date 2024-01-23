from django.contrib import admin
from .models import Blog,Tag

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_on')
    search_field = ['title', 'content']

admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag)

