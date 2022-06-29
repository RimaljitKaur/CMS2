# Generated by Django 4.0.4 on 2022-06-21 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0005_remove_student_detail_course_registered_students'),
    ]

    operations = [
        migrations.CreateModel(
            name='registered_student',
            fields=[
                ('roll_no', models.AutoField(primary_key=True, serialize=False)),
                ('course', models.CharField(choices=[('1', 'B.A.'), ('2', 'B.Sc-(Non-Medical)'), ('3', 'B.Sc-IT'), ('4', 'B.Sc{Hons.}'), ('5', 'M.Sc-IT'), ('6', 'M.A.')], max_length=50)),
                ('section', models.CharField(max_length=10)),
                ('app_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentapp.student_detail')),
            ],
        ),
        migrations.DeleteModel(
            name='registered_students',
        ),
    ]