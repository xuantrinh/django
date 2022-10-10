from django.db import models
from ..category.model import Category

class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        db_column='category_id'
    )
    name = models.CharField(
        max_length=200,
        db_column='name')

    title = models.CharField(
        max_length=200,
        db_column='title')

    price = models.FloatField(db_column='price')

    image = models.URLField(
        max_length=200,
        db_column='image')

    score = models.FloatField(
        null=True,
        default=None,
        db_column='score')

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at')

    updated_at = models.DateTimeField(
        auto_now=True,
        db_column='updated_at')

    def __str__(self):
        return f'Category: {self.category}, Name: {self.name}'

    class Meta:
        db_table = 'tbl_product'
        ordering = ['id']