# Generated by Django 4.1.5 on 2023-06-08 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_competition'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('utr', models.CharField(max_length=255)),
            ],
        ),
    ]
