# Generated by Django 2.2.6 on 2019-11-19 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Age_group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('age_arange', models.CharField(max_length=100)),
                ('age_total', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Country_group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('country_total', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Visa_group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('visa_type', models.CharField(max_length=100)),
                ('visa_total', models.IntegerField(default=0)),
            ],
        ),
    ]
