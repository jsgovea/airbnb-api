# Generated by Django 3.2.9 on 2021-11-27 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_auto_20191216_0937'),
        ('users', '0002_auto_20211126_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='favs',
            field=models.ManyToManyField(blank=True, null=True, related_name='favs', to='rooms.Room'),
        ),
    ]