# Generated by Django 3.0.3 on 2021-02-02 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthcareApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='logins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.CharField(max_length=100)),
            ],
        ),
    ]
