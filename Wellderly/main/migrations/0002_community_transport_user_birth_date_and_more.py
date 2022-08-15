# Generated by Django 4.1 on 2022-08-15 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='birth_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='emergency_contact',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('place', models.CharField(max_length=200)),
                ('date_time', models.DateTimeField()),
                ('description', models.TextField()),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.community')),
                ('transport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.transport')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
    ]