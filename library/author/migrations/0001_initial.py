# Generated by Django 3.1.1 on 2020-09-24 23:51

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),  # Ім'я автора
                ('last_name', models.CharField(max_length=255)),   # Прізвище автора
                ('birth_date', models.DateField(null=True, blank=True)),  # Дата народження автора (необов'язково)
                ('biography', models.TextField(null=True, blank=True)),  # Біографія автора
            ],
        ),
    ]
