# Generated by Django 3.1 on 2020-09-25 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0005_list_reunion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='reunion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='connect.reunion'),
        ),
    ]
