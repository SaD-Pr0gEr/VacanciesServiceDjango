# Generated by Django 3.2 on 2022-04-15 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20220405_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='billing_from',
            field=models.BigIntegerField(help_text='в долларах США', verbose_name='Зарплата(от-)'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='billing_to',
            field=models.BigIntegerField(help_text='в долларах США', verbose_name='Зарплата(до-)'),
        ),
    ]
