from django.contrib import admin
from.models import*
# Register your models here.
class stddetails(admin.ModelAdmin):
    list_display=["idnum","Name","Gender","course","duration","phnum","place"]
    search_fields=["Name"]
admin.site.register(students_details,stddetails)

admin.site.register(course)