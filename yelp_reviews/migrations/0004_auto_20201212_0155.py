# Generated by Django 3.1.4 on 2020-12-12 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yelp_reviews', '0003_auto_20201211_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factreview',
            name='useful',
            field=models.IntegerField(default=0),
        ),
    ]
