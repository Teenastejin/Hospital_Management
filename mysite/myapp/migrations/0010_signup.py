# Generated by Django 4.2 on 2023-05-05 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('pswrd', models.CharField(max_length=250)),
                ('cnfrmpswrd', models.CharField(max_length=250)),
            ],
        ),
    ]
