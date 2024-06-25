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
class Resource(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,
                                 related_name='category')
    filter_category = models.ForeignKey(FilterCategories, on_delete=models.SET_NULL, null=True,
                                        related_name='filter_category')
    filters = models.ForeignKey(Filters, on_delete=models.SET_NULL, null=True,
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




class Interive(BaseModel):

    class Status(models.TextChoices):
        GALLERY = 'Gl', 'Gallery'
        AUDIO = 'AU', 'Audio'
        FILE = 'Fl', 'File'
        VIRTUAL_REALITY = 'VR', 'Virtual_reality'
        VIDEO = 'VD', 'Video'
        LOCATION = 'LN','Location'


    status = models.CharField(max_length=20,
                              choices=Status.choices,
                              default=Status.GALLERY)
    title = models.CharField(max_length=155)
    file = models.FileField(upload_to='media/files/resource',blank=True,null=True)
    link = models.URLField(blank=True, null=True)
    latitude = models.CharField(max_length=500, blank=True, null=True)
    longitude = models.CharField(max_length=500, blank=True, null=True)
    resource_interive = models.ForeignKey(Resource, on_delete=models.SET_NULL, null=True,
                                           related_name='resource_interive')



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

