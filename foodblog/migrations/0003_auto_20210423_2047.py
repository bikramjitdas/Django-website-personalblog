# Generated by Django 3.1.7 on 2021-04-23 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodblog', '0002_post_mins_read'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-pk']},
        ),
        migrations.AddField(
            model_name='post',
            name='read_count',
            field=models.IntegerField(default=0),
        ),
    ]