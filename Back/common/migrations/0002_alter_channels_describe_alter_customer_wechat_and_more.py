# Generated by Django 4.1 on 2023-02-03 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channels',
            name='describe',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='wechat',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='describe',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]