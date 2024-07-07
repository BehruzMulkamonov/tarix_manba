from django.db import models


class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=255)
    icon = models.FileField(blank=True, null=True , upload_to="icons/")  # shunga iconca kodi yozilidi
    image = models.FileField(blank=True, null=True , upload_to="icons/")  # shunga iconca kodi yozilidi
    order = models.IntegerField()
    interactive = models.BooleanField()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class PeriodFilter(BaseModel):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,
                                 related_name='category_filter')

    class Meta:
        verbose_name = 'Period Filter'
        verbose_name_plural = 'Period Filters'

    def __str__(self):
        return self.title


class FilterCategories(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,
                                 related_name='categories')
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Filter Category'
        verbose_name_plural = 'Filter Categories'

    def __str__(self):
        return self.title


class Filters(BaseModel):
    filter_category = models.ForeignKey(FilterCategories, on_delete=models.SET_NULL, null=True,
                                        related_name='filters_category')
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Filter'
        verbose_name_plural = 'Filters'

    def __str__(self):
        return self.title

class Province(BaseModel):
    title = models.CharField(max_length=255,blank=True, null=True)
    latitude = models.CharField(max_length=500, blank=True, null=True)
    longitude = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Province'
        verbose_name_plural = 'Provinces'



# class Interive(BaseModel):

#     class Status(models.TextChoices):
#         GALLERY = 'Gl', 'Gallery'
#         AUDIO = 'AU', 'Audio'
#         FILE = 'Fl', 'File'
#         VIRTUAL_REALITY = 'VR', 'Virtual_reality'
#         VIDEO = 'VD', 'Video'
#         LOCATION = 'LN','Location'


#     status = models.CharField(max_length=20,
#                               choices=Status.choices,
#                               default=Status.GALLERY)
#     title = models.CharField(max_length=155)
#     file = models.FileField(upload_to='media/files/resource',blank=True,null=True)
#     link = models.URLField(blank=True, null=True)
#     latitude = models.CharField(max_length=500, blank=True, null=True)
#     longitude = models.CharField(max_length=500, blank=True, null=True)




class Resource(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,
                                 related_name='category')
    filter_category = models.ForeignKey(FilterCategories, on_delete=models.SET_NULL, null=True,
                                        related_name='filter_category')
    filters = models.ManyToManyField(Filters,  blank=True,
                                related_name='filters')
    period_filter = models.ForeignKey(PeriodFilter, on_delete=models.SET_NULL, null=True,
                                      related_name='period_filter')
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/images/resource',blank=True,null=True)
    content = models.TextField()
    statehood = models.BooleanField(default=True)
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True,
                                 related_name='select_province')




    class Meta:
        verbose_name = 'Resource'
        verbose_name_plural = 'Resources'

    def __str__(self):
        return self.title


class Gallery(BaseModel):
    resource_gallery = models.ForeignKey(Resource, on_delete=models.SET_NULL, null=True,
                                           related_name='resource_gallery')
    title = models.CharField(max_length=155)
    image = models.ImageField(upload_to='media/files/resource',blank=True,null=True)

class File(BaseModel):
    resource_file = models.ForeignKey(Resource, on_delete=models.SET_NULL, null=True,
                                           related_name='resource_file')
    title = models.CharField(max_length=155)
    file = models.FileField(upload_to='media/files/resource',blank=True,null=True)

class Audio(BaseModel):
    resource_audio = models.ForeignKey(Resource, on_delete=models.SET_NULL, null=True,
                                           related_name='resource_audio')
    title = models.CharField(max_length=155)
    file = models.FileField(upload_to='media/files/resource',blank=True,null=True)

class Virtual_reality(BaseModel):
    resource_virtual_reality = models.ForeignKey(Resource, on_delete=models.SET_NULL, null=True,
                                           related_name='resource_virtual_reality')
    title = models.CharField(max_length=155)
    file = models.FileField(upload_to='media/files/resource',blank=True,null=True)


class Video(BaseModel):
    resource_video = models.ForeignKey(Resource, on_delete=models.SET_NULL, null=True,
                                           related_name='resource_video')
    title = models.CharField(max_length=155)
    link = models.URLField(blank=True, null=True)

class Location(BaseModel):
    resource_location = models.ForeignKey(Resource, on_delete=models.SET_NULL, null=True,
                                           related_name='resource_location')
    title = models.CharField(max_length=155)
    latitude = models.CharField(max_length=500, blank=True, null=True)
    longitude = models.CharField(max_length=500, blank=True, null=True)



class Attributes(BaseModel):
    resource_attribute = models.ForeignKey(Resource, on_delete=models.SET_NULL, null=True,
                                           related_name='resource_attribute')
    attributes_title = models.CharField(max_length=255)
    attributes_description = models.CharField(max_length=255)



class Contents(BaseModel):
    resource_content = models.ForeignKey(Resource, on_delete=models.SET_NULL, null=True,
                                         related_name='resource_content')
    contents_title = models.CharField(max_length=255)
    contents_description = models.TextField()

