# Generated by Django 4.0.1 on 2022-01-26 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('capital', models.CharField(max_length=100)),
                ('area', models.IntegerField(help_text='(in square kilometers)')),
            ],
        ),
    ]
