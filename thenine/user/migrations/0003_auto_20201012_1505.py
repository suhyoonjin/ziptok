# Generated by Django 3.1.1 on 2020-10-12 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20201011_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_expert',
            field=models.CharField(max_length=10, null=True, verbose_name='전문가여부'),
        ),
    ]
