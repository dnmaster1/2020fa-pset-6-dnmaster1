# Generated by Django 3.1.4 on 2020-12-12 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yelp_reviews', '0005_auto_20201212_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factreview',
            name='cool',
            field=models.IntegerField(max_length=1),
        ),
    ]
