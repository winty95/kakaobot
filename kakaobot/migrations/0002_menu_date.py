# Generated by Django 2.0.7 on 2018-08-05 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kakaobot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='date',
            field=models.CharField(default='', max_length=30),
        ),
    ]
