# Generated by Django 3.0.8 on 2020-07-21 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=50)),
                ('s_age', models.IntegerField()),
                ('s_roll', models.CharField(max_length=10)),
                ('s_email', models.EmailField(max_length=100)),
            ],
        ),
    ]
