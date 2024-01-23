from django.contrib import admin
from .models  import Report


# Register your models here.
class ReportAdmin(admin.ModelAdmin):
	list_display = ('title', 'created_on', 'author')

admin.site.register(Report, ReportAdmin)
