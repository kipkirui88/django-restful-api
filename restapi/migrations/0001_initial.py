# Generated by Django 4.1.5 on 2023-06-13 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adm', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
            ],
        ),
    ]
