# Generated by Django 3.2.7 on 2021-10-20 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blogpost_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]