# Generated by Django 4.2.3 on 2023-07-26 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=30)),
                ('birthDate', models.DateField()),
                ('telephone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=20)),
                ('image', models.CharField(max_length=1500)),
                ('userName', models.CharField(max_length=30, unique=True)),
            ],
        ),
    ]