from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }
    list_display = (
        'name',
        'slug',
    )
    list_filter = (
        'name',
    )


@admin.register(models.Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }
    list_display = (
        'name',
        'description',
        'slug',
        'image_tag',
        'price',
        'discount',
        'quantity',
        'category',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'category',
    )

    @admin.display(description='Изображение')
    def image_tag(self, product: models.Products):
        if product.image:
            return mark_safe(
                f'<img src={product.image.url} width="80" height="60">'
            )
        return 'Без фото'
