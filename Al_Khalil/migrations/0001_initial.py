# Generated by Django 4.2 on 2023-04-28 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jai_Namaz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('photo', models.ImageField(upload_to='jai_namaz')),
                ('price', models.IntegerField()),
            ],
        ),
    ]