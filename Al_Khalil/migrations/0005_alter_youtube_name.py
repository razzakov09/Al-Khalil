# Generated by Django 4.2 on 2023-04-29 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Al_Khalil', '0004_youtube'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtube',
            name='name',
            field=models.URLField(max_length=500),
        ),
    ]
