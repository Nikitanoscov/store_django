from django.db import models


class Category(models.Model):

    name = models.CharField(
        verbose_name='Категория',
        max_length=150,
        unique=True
    )
    slug = models.SlugField(
        verbose_name='URL',
        max_length=200,
        unique=True,
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'category'
        verbose_name = "категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Products(models.Model):

    name = models.CharField(
        verbose_name='Название',
        max_length=150,
        unique=True
    )
    slug = models.SlugField(
        verbose_name='URL',
        max_length=200,
        unique=True,
        blank=True,
        null=True
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='goods_images',
        blank=True,
        null=True
    )
    price = models.DecimalField(
        default=0.00,
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена'
    )
    discount = models.DecimalField(
        default=0.00,
        max_digits=10,
        decimal_places=2,
        verbose_name='Скидка в %'
    )
    quantity = models.PositiveIntegerField(
        default=0,
        verbose_name='Количество'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория'
    )

    class Meta:
        db_table = 'product'
        verbose_name = "товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        """Метод для вывода name."""
        return self.name

    def display_id(self):
        """Метод для форматированного вывода id."""
        return f'{self.id:05}'

    def sell_price(self):
        """Метод для перерасчета цены при наличии скидки."""
        if self.discount:
            return round(self.price - (self.price/100 * self.discount), 2)
        return self.price
