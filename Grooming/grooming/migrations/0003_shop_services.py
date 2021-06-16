# Generated by Django 3.0.3 on 2020-04-03 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grooming', '0002_shops_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='shop_services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254)),
                ('Service', models.CharField(max_length=25)),
                ('Price', models.IntegerField()),
            ],
        ),
    ]
