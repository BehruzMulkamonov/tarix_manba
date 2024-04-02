from django.db import models
from ckeditor.fields import RichTextField


class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)  # shunga iconca kodi yozilidi
    order = models.IntegerField()
    interactive = models.BooleanField()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class PeriodFilter(BaseModel):
    title = RichTextField(null=True, blank=True)

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
    image = models.ImageField(upload_to='media/images/resource', blank=True, null=True)
    content = RichTextField()
    statehood = models.BooleanField()
    province = models.CharField(max_length=255)  # type 12 ta viloyat
    interive_content = models.CharField(max_length=255)  # buni type qilib vedio,audio,
    interive_title = models.CharField(max_length=255)  # bu ham inline va counti bilan
    interive_file = models.FileField(upload_to='media/files/resource', blank=True, null=True)

    class Meta:
        verbose_name = 'Resource'
        verbose_name_plural = 'Resources'

    def __str__(self):
        return self.title


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
