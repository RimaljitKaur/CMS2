# Generated by Django 4.0.4 on 2022-06-21 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0006_registered_student_delete_registered_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_detail',
            name='application_no',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
