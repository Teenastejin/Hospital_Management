from django.contrib import admin
from .models import Department,Doctors,Booking,Job



admin.site.register(Booking)
admin.site.register(Department)
admin.site.register(Doctors)
admin.site.register(Job)


# Register your models here.
