# Generated by Django 3.0 on 2019-12-14 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20191214_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='descriptions',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='telephone',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
