# Generated by Django 4.2.5 on 2023-09-20 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('password', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
