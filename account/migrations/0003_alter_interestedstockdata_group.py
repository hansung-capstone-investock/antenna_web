# Generated by Django 3.2 on 2021-05-23 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210523_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interestedstockdata',
            name='group',
            field=models.CharField(max_length=50, null=True),
        ),
    ]