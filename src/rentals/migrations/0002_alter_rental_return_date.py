# Generated by Django 4.2.4 on 2023-08-16 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='return_date',
            field=models.DateField(blank=True, help_text='actual return date', null=True),
        ),
    ]
