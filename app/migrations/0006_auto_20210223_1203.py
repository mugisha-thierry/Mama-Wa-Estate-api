# Generated by Django 3.1.5 on 2021-02-23 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_category_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductMerch',
        ),
        migrations.AlterField(
            model_name='vendor',
            name='password',
            field=models.CharField(max_length=200),
        ),
    ]