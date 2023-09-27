from django.contrib import admin
# from . models import StudentData,Catogory,Product,Color,Page
from . models import StudentData


class StudentAdmin(admin.ModelAdmin):
    list_display = ["student_name","student_address"]





admin.site.register(StudentData,StudentAdmin)
# admin.site.register(Catogory)
# admin.site.register(Product)
# admin.site.register(Color)
# admin.site.register(Page)


# Register your models here.
