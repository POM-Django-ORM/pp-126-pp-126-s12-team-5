# Generated by Django 3.1.1 on 2020-09-24 23:51

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=models.CASCADE, to='authentication.CustomUser')),  # Зв'язок з користувачем
                ('book', models.ForeignKey(on_delete=models.CASCADE, to='book.Book')),  # Зв'язок з книгою
                ('created_at', models.DateTimeField(auto_now_add=True)),  # Дата створення замовлення
                ('plated_end_at', models.DateTimeField()),  # Запланована дата завершення
                ('end_at', models.DateTimeField(null=True, blank=True)),  # Дата завершення
            ],
        ),
    ]
