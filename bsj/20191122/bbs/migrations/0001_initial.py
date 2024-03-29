# Generated by Django 2.2.6 on 2019-11-19 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bbs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('mid', models.CharField(max_length=100)),
                ('udate', models.DateTimeField(auto_now=True)),
                ('user_nick', models.CharField(max_length=100, null=True)),
                ('user_country', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oid', models.IntegerField(default=0)),
                ('mid', models.CharField(max_length=100, null=True)),
                ('user_nick', models.CharField(max_length=100)),
                ('review_content', models.TextField(default='')),
                ('udate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
