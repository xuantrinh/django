from django.db import models

class Category(models.Model):
    name = models.CharField(
        max_length=200,
        db_column='name'
    )

    description = models.CharField(
        max_length=600,
        db_column='description'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        db_column='updated_at'
    )

    def __str__(self):
        return f'Name: {self.name}, Description: {self.description}'

    class Meta:
        db_table = 'tbl_category'
        ordering = ['id']