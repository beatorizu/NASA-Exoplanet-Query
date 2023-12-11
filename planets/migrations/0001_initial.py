# Generated by Django 5.0 on 2023-12-11 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_of_discovery', models.IntegerField()),
                ('discovery_method', models.CharField(max_length=30)),
                ('hostname', models.CharField(max_length=30)),
                ('discovery_facility', models.CharField(max_length=30)),
            ],
        ),
    ]