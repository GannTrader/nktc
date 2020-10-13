# Generated by Django 3.1.1 on 2020-10-10 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_auto_20201010_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], default='inactive', max_length=25),
        ),
        migrations.AddField(
            model_name='reply',
            name='status',
            field=models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], default='inactive', max_length=25),
        ),
    ]