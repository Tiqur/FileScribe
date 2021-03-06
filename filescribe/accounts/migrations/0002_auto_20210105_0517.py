# Generated by Django 3.1.4 on 2021-01-05 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fs_user',
            options={'verbose_name': 'User'},
        ),
        migrations.AddField(
            model_name='fs_user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='fs_user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
