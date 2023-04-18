# Generated by Django 4.1.7 on 2023-04-10 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('director', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=25)),
                ('sport', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='schools.sport')),
            ],
        ),
    ]