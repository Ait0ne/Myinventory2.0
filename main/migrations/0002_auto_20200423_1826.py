# Generated by Django 3.0.5 on 2020-04-23 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='111.jpg', upload_to='uploads'),
        ),
    ]