# Generated by Django 4.0.4 on 2022-05-17 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('text', models.CharField(max_length=300)),
                ('created_date', models.DateTimeField()),
                ('uploaded_date', models.DateTimeField()),
            ],
        ),
    ]
