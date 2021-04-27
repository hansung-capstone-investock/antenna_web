# Generated by Django 3.1.7 on 2021-04-26 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='companyData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='dcData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='fmkorData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MainNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=1000)),
                ('summary', models.TextField()),
                ('publishDay', models.CharField(max_length=100)),
                ('link', models.TextField()),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]
