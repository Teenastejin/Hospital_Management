# Generated by Django 4.2 on 2023-05-03 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='dep_img',
            field=models.ImageField(default=1, upload_to='departments'),
            preserve_default=False,
        ),
    ]
