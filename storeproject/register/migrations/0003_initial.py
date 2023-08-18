# Generated by Django 4.2.3 on 2023-08-18 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register', '0002_delete_coursemodel_delete_departmentmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseModel',
            fields=[
                ('Cid', models.IntegerField(primary_key=True, serialize=False)),
                ('Cname', models.CharField(max_length=100)),
                ('Did', models.IntegerField()),
            ],
            options={
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='DepartmentModel',
            fields=[
                ('Did', models.IntegerField(primary_key=True, serialize=False)),
                ('Dname', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'department',
            },
        ),
    ]