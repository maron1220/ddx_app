# Generated by Django 3.0.4 on 2021-06-02 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello_ddx', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ddxlist',
            name='bt_category',
            field=models.CharField(default='None', max_length=30),
        ),
        migrations.AddField(
            model_name='ddxlist',
            name='upperzero_lowerone',
            field=models.IntegerField(default=0),
        ),
    ]
