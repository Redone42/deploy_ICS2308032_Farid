# Generated by Django 5.1 on 2024-09-23 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0005_mentor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('description', models.TextField(max_length=50)),
            ],
        ),
    ]