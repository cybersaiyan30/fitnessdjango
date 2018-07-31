# Generated by Django 2.0.7 on 2018-07-26 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0005_diet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diet',
            name='breakfast_detail',
        ),
        migrations.RemoveField(
            model_name='diet',
            name='dinner_detail',
        ),
        migrations.RemoveField(
            model_name='diet',
            name='lunch_detail',
        ),
        migrations.AddField(
            model_name='diet',
            name='breakfast',
            field=models.CharField(default='hello', max_length=2200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diet',
            name='dinner',
            field=models.CharField(default='hello', max_length=2200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diet',
            name='lunch',
            field=models.CharField(default='hello', max_length=2200),
            preserve_default=False,
        ),
    ]