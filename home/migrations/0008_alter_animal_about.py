# Generated by Django 3.2.7 on 2021-10-18 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_contactmodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='about',
            field=models.TextField(max_length=200),
        ),
    ]
