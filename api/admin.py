from django.contrib import admin
from .models import Student, Organisation, Scholarship

# Register your models here.
admin.site.register(Student)
admin.site.register(Organisation)
admin.site.register(Scholarship)