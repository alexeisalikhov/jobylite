# Generated by Django 2.0.3 on 2018-04-25 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_remove_job_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(blank=True, max_length=5000),
        ),
    ]
