# Generated by Django 3.1 on 2020-10-05 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20201003_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pic',
            field=models.ImageField(blank=True, default='', null=True, upload_to='Static/Blog'),
        ),
    ]
