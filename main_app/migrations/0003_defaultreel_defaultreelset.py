# Generated by Django 2.2.7 on 2019-11-23 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20191123_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultReel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('field0', models.CharField(default='1', max_length=30)),
                ('field1', models.CharField(default='2', max_length=30)),
                ('field2', models.CharField(default='3', max_length=30)),
                ('field3', models.CharField(default='4', max_length=30)),
                ('field4', models.CharField(default='5', max_length=30)),
                ('field5', models.CharField(default='6', max_length=30)),
                ('field6', models.CharField(default='7', max_length=30)),
                ('field7', models.CharField(default='8', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='DefaultReelSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('reels', models.ManyToManyField(to='main_app.DefaultReel', verbose_name='list of default reels')),
            ],
        ),
    ]
