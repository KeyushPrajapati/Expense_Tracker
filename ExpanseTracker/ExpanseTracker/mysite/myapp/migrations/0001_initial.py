# Generated by Django 4.2.3 on 2023-07-25 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('amount', models.FloatField()),
                ('category', models.CharField(max_length=50)),
            ],
        ),
    ]
