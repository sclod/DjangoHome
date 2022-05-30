# Generated by Django 4.0.4 on 2022-05-21 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
        ('students', '0006_alter_student_age_alter_student_first_name_and_more'),
        ('group', '0003_remove_group_creation_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='students',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='students.student'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='teacher',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='teachers.teachers'),
            preserve_default=False,
        ),
    ]
