# Generated by Django 2.2.7 on 2019-11-23 23:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultReel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(null=True)),
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
            name='Reel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(null=True)),
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
            name='ReelSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('reels', models.ManyToManyField(to='main_app.Reel', verbose_name='list of reels')),
            ],
            options={
                'ordering': ['owner'],
            },
        ),
        migrations.CreateModel(
            name='DefaultReelSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(null=True)),
                ('reels', models.ManyToManyField(to='main_app.DefaultReel', verbose_name='list of default reels')),
            ],
        ),
    ]
