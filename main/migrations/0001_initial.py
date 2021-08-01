# Generated by Django 2.0.5 on 2021-07-25 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture_title', models.CharField(max_length=2000)),
                ('lecture_content', models.TextField()),
                ('lecture_published', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
