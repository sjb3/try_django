# Generated by Django 2.1.5 on 2019-01-26 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190126_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
