# Generated by Django 3.0.3 on 2021-11-22 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='First Name')),
                ('fname', models.CharField(max_length=500, verbose_name="Father's Name")),
                ('lname', models.CharField(max_length=500, verbose_name='Surname')),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('pin', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('manufacturers', models.CharField(choices=[('Covaxin', 'Covaxin (Bharat Biotech)'), ('Covishield', 'Covishield (Serum Institute of India)'), ('Sputnik', 'Sputnik V')], max_length=50)),
                ('doses', models.CharField(choices=[('1st', 'First Dose'), ('2nd', 'Second Dose')], max_length=50)),
                ('dov', models.DateField(verbose_name='Date of Vaccination')),
            ],
        ),
    ]