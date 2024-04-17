from django.contrib import admin
from other_app.models import Library_Category, Feedbacks, Library, About, Comments, Connection, Event, News, Sliders
from modeltranslation.admin import TranslationAdmin

admin.site.register(Library_Category)
admin.site.register(Library)
admin.site.register(News)
admin.site.register(Event)
admin.site.register(Feedbacks)
admin.site.register(Comments)
admin.site.register(Connection)
admin.site.register(Sliders)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'content',)
    fields = ('title_uz','title_ru','title_en', 'content_uz', 'content_ru', 'content_en')
