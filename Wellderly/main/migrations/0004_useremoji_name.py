# Generated by Django 4.1 on 2022-08-22 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_emoji_useremoji'),
    ]

    operations = [
        migrations.AddField(
            model_name='useremoji',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
