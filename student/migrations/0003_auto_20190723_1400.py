# Generated by Django 2.2.1 on 2019-07-23 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_student_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Courses',
            field=models.ManyToManyField(to='course.Course'),
        ),
    ]
