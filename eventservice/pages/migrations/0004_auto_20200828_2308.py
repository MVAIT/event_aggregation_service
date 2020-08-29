# Generated by Django 3.0.2 on 2020-08-28 20:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20200828_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='events',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='End'),
        ),
        migrations.AddField(
            model_name='events',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Start'),
        ),
        migrations.AlterField(
            model_name='events',
            name='location',
            field=models.TextField(default='no location', max_length=1000),
        ),
    ]
