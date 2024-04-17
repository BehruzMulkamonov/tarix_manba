from modeltranslation.translator import translator, TranslationOptions
from modeltranslation.decorators import register
from other_app.models import About, Comments, Connection, Event, Feedbacks, Library, Library_Category, News, Sliders


# About
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'content',) 

translator.register(About, AboutTranslationOptions)

# Comment 
class CommentTranslationOptions(TranslationOptions):
    fields = ('message', ) 

translator.register(Comments, CommentTranslationOptions)

# Connection
class ConnectionTranslationOptions(TranslationOptions):
    fields = ('address', 'location', 'map') 

translator.register(Connection, ConnectionTranslationOptions)

# Event
class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'content',) 

translator.register(Event, EventTranslationOptions)

# feedback
class FeedbackTranslationOptions(TranslationOptions):
    fields = ('message',) 

translator.register(Feedbacks, FeedbackTranslationOptions)

# libarary_category
class Library_Cat_TranslationOptions(TranslationOptions):
    fields = ('title',) 

translator.register(Library_Category, Library_Cat_TranslationOptions)

# library
class LibraryTranslationOptions(TranslationOptions):
    fields = ('title', 'author', 'type', 'country', 'language') 

translator.register(Library, LibraryTranslationOptions)

# news
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content') 

translator.register(News, NewsTranslationOptions)

# sliders
class SlidersTranslationOptions(TranslationOptions):
    fields = ('title',) 

translator.register(Sliders, SlidersTranslationOptions)