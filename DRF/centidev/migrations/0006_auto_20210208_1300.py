# Generated by Django 3.0.1 on 2021-02-08 17:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('centidev', '0005_auto_20210208_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='fe_update',
            field=models.CharField(blank=True, db_column='Fe_Update', default=django.utils.timezone.now, max_length=50, null=True),
        ),
    ]