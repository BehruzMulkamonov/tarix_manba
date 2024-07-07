from django.contrib import admin
from .models import Category, FilterCategories, PeriodFilter, Filters,  Resource, Province, Gallery, File, Audio, Virtual_reality, Video, Location

admin.site.register(Category)
admin.site.register(FilterCategories)
admin.site.register(PeriodFilter)
admin.site.register(Filters)
# admin.site.register(Interive)
admin.site.register(Resource)
admin.site.register(Province)

admin.site.register(Gallery)
admin.site.register(Video)
admin.site.register(Virtual_reality)
admin.site.register(Location)
admin.site.register(Audio)
admin.site.register(File)

