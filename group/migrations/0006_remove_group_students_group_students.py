# Generated by Django 4.0.4 on 2022-05-22 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_alter_student_age_alter_student_first_name_and_more'),
        ('group', '0005_remove_group_students_group_students'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='students',
        ),
        migrations.AddField(
            model_name='group',
            name='students',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='students.student'),
            preserve_default=False,
        ),
    ]