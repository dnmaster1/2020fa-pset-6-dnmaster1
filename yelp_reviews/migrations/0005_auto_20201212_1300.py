# Generated by Django 3.1.4 on 2020-12-12 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yelp_reviews', '0004_auto_20201212_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dimdate',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
