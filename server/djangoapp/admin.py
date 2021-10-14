from django.contrib import admin
# from .models import related models


# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 3

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    fields = ('name', 'description')

# Register models here
admin.site.register(CarModel)
admin.site.register(CarMake, CarMakeAdmin)
