# Generated by Django 4.0.4 on 2022-06-20 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetail',
            fields=[
                ('rollno', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('marks', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='studentdetails',
        ),
    ]
