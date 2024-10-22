# Generated by Django 5.1 on 2024-09-05 15:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('title', models.TextField(max_length=100)),
                ('author', models.TextField(max_length=40)),
                ('published_year', models.IntegerField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('student_name', models.TextField(max_length=50)),
                ('student_phone', models.CharField(max_length=10)),
                ('student_email', models.TextField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Borrowing',
            fields=[
                ('borrow_id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('borrow_date', models.DateField(max_length=10)),
                ('return_date', models.DateField(max_length=10)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Library.book')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Library.student')),
            ],
        ),
    ]
