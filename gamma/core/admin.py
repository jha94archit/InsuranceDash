from django.contrib import admin
from .models import Fuel, Vehicle_Segment, Customer_Region, Customer_Income_Group, Policy

# Register your models here.
admin.site.register(Fuel)
admin.site.register(Vehicle_Segment)
admin.site.register(Customer_Region)
admin.site.register(Customer_Income_Group)
admin.site.register(Policy)
