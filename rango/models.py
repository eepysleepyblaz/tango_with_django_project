from django.db import models

#Pg97 TwD
from django.template.defaultfilters import slugify

# Create your models here.

#Pg68 TwD
class Category(models.Model):

    #Pg129 TwD
    NAME_MAX_LENGTH = 128

    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)

    #Pg87 Twd
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    #Pg 97
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    #Pg78 TwD
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Page(models.Model):

    #Pg129 TwD
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    url = models.URLField()
    views = models.IntegerField(default=0)


    def __str__(self):
        return self.title
    
