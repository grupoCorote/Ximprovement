# Generated by Django 3.0.7 on 2020-07-20 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frigobar', '0007_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='First name'),
        ),
    ]
