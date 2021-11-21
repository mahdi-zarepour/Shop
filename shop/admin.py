from django.contrib import admin
from .models import Category, Product



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'name', 'is_subcategory')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'name', 'price', 'available')
    list_filter = ('available',)
    search_fields = ('name', 'description')
    list_editable = ('price', 'available')
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ('category',)
    actions = ('make_available', 'make_unavailable')


    def make_available(self, request, queryset):
        # queryset: selected object and return count of selected
        rows = queryset.update(available=True)
        self.message_user(request, f'{rows} items change to available')
    make_available.short_description = 'make all available'

    def make_unavailable(self, request, queryset):
        # queryset: selected object and return count of selected
        rows = queryset.update(available=False)
        self.message_user(request, f'{rows} items change to unavailable')
    make_unavailable.short_description = 'make all unavailable'
    