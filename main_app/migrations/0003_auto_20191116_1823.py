# Generated by Django 2.2.7 on 2019-11-16 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20191116_1749'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlotSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('slot0', models.CharField(max_length=30)),
                ('slot1', models.CharField(max_length=30)),
                ('slot2', models.CharField(max_length=30)),
                ('slot3', models.CharField(max_length=30)),
                ('slot4', models.CharField(max_length=30)),
                ('slot5', models.CharField(max_length=30)),
                ('slot6', models.CharField(max_length=30)),
                ('slot7', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['owner'],
            },
        ),
        migrations.DeleteModel(
            name='Slot',
        ),
    ]
