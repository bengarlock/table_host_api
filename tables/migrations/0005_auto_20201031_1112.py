# Generated by Django 3.1.2 on 2020-10-31 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0004_remove_table_reservation_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='reservation_id',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='table',
            name='restaurant_id',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]