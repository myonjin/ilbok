# Generated by Django 3.2.13 on 2023-03-22 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='All_in_one',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'all_in_one',
                'managed': False,
            },
        ),
    ]
