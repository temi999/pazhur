# Generated by Django 2.2.7 on 2019-12-13 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_defaultreel_leave_empty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaultreel',
            name='name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='defaultreelset',
            name='name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='reel',
            name='name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='reelset',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]
