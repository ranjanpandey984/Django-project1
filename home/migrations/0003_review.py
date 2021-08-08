# Generated by Django 3.2.6 on 2021-08-08 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('designation', models.CharField(max_length=500)),
                ('comment', models.TextField(max_length=500)),
                ('image', models.TextField(max_length=500)),
            ],
        ),
    ]
