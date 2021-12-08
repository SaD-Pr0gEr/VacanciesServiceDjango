# Generated by Django 3.2 on 2021-11-20 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=260, unique=True, verbose_name='email пользователя')),
                ('subscribed', models.BooleanField(default=False, verbose_name='Подписка на рассылку')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активный аккаунт')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Статус персонала')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='city_users', to='main_app.cities', verbose_name='Ваш город')),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lang_users', to='main_app.programlanguage', verbose_name='Ваш язык программирования')),
            ],
            options={
                'verbose_name': 'Пользователи',
                'verbose_name_plural': 'Список пользателей',
            },
        ),
    ]