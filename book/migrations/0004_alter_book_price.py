# Generated by Django 5.0.6 on 2024-05-26 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_book_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.CharField(blank=True, null=True),
        ),
    ]
