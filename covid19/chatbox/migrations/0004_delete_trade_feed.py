# Generated by Django 3.0.3 on 2020-05-15 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbox', '0003_delete_raise_issue'),
    ]

    operations = [
        migrations.DeleteModel(
            name='trade_feed',
        ),
    ]