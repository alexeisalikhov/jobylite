# Generated by Django 2.0.3 on 2018-05-07 13:34

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_auto_20180425_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, max_length=5000),
        ),
    ]
