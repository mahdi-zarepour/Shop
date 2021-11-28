from django.db import models
from django.urls import reverse



class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='nested_category', null=True, blank=True)
    is_subcategory = models.BooleanField(default=False)


    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('shop:category_product_list', args=(self.slug,))



class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/')
    description = models.TextField()
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category, related_name='products')


    class Meta:
        ordering = ('name',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('shop:product_detail', args=(self.slug,))