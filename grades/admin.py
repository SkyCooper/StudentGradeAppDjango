from django.contrib import admin
from .models import (Teacher, Students, Grade, Lessons)

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Students)
admin.site.register(Grade)
admin.site.register(Lessons)