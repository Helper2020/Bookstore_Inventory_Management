# Generated by Django 3.2.8 on 2021-10-24 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_manager', '0003_supportticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supportticket',
            name='message',
            field=models.TextField(max_length=500),
        ),
    ]