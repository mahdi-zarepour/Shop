from django.contrib import admin
from .models import Order, Item, Coupon



class ItemInline(admin.TabularInline):
    model = Item
    raw_id_fields = (
        'product',
        )



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id',
    '__str__',
    'created',
    'updated',
    'paid',
    )
    search_fields = (
        'user',
    )
    list_filter = (
        'paid',
        )
    actions = (
        'was_paid',
        'not_paid',
        )
    inlines = (
        ItemInline,
        )


    def was_paid(self, request, queryset):
        # queryset: selected object and return count of selected
        rows = queryset.update(paid=True)
        self.message_user(request, f'{rows} paid True')
    was_paid.short_description = 'True payment'

    def not_paid(self, request, queryset):
        # queryset: selected object and return count of selected
        rows = queryset.update(paid=False)
        self.message_user(request, f'{rows} not paid')
    not_paid.short_description = 'Flase payment'



@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'valid_from',
        'valid_to',
        'discount',
        'active',
        )
    list_editable = (
        'discount',
        'active',
        )
    list_filter = (
        'active',
    )
    search_fields = (
        'code',
    )