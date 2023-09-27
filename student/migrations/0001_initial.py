# Generated by Django 4.2.5 on 2023-09-12 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=50)),
                ('student_addresss', models.CharField(max_length=50)),
                ('student_contact', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'StudentData',
            },
        ),
    ]
