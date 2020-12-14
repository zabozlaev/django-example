# Generated by Django 3.1.4 on 2020-12-14 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_url', models.URLField()),
                ('short_url', models.CharField(max_length=16)),
            ],
        ),
    ]
