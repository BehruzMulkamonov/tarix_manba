from django.contrib import admin
from .models import Category, FilterCategories, PeriodFilter, Filters

admin.site.register(Category)
admin.site.register(FilterCategories)
admin.site.register(PeriodFilter)
admin.site.register(Filters)
