from django.contrib import admin
from.models import category,unit,item,supplier,Order,Employee

# Register your models here.
admin.site.register(category)
admin.site.register(unit)
admin.site.register(item)
admin.site.register(supplier)
admin.site.register(Order)
admin.site.register(Employee)

