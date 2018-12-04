# Generated by Django 2.0.3 on 2018-04-09 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('photo', models.ImageField(blank=True, upload_to='photos/')),
                ('cv', models.FileField(blank=True, upload_to='cvs/')),
                ('doc', models.FileField(blank=True, upload_to='docs/')),
                ('text', models.TextField(blank=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Job')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
