# Generated by Django 4.2 on 2023-04-29 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Al_Khalil', '0003_alter_book_photo_alter_tasbih_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Youtube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.URLField()),
            ],
        ),
    ]
