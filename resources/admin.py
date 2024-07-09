from django.contrib import admin
from .models import Category, FilterCategories, PeriodFilter, Filters,  Resource, Province, Interive

admin.site.register(Category)
admin.site.register(FilterCategories)
admin.site.register(PeriodFilter)
admin.site.register(Filters)
admin.site.register(Interive)
admin.site.register(Resource)
admin.site.register(Province)



