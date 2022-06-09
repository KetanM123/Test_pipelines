# Generated by Django 4.0.2 on 2022-02-21 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('music_genre', models.CharField(max_length=255)),
                ('daily_practice_time', models.IntegerField()),
                ('days', models.IntegerField()),
                ('days_practiced', models.IntegerField()),
            ],
        ),
    ]
