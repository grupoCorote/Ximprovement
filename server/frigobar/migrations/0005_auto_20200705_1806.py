# Generated by Django 3.0.7 on 2020-07-05 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frigobar', '0004_auto_20200705_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='-', max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]
