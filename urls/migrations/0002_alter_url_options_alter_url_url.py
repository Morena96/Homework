# Generated by Django 4.1.2 on 2022-10-27 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urls', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='url',
            options={'verbose_name_plural': 'Urls'},
        ),
        migrations.AlterField(
            model_name='url',
            name='url',
            field=models.CharField(max_length=200),
        ),
    ]
