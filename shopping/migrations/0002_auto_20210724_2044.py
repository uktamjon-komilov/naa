# Generated by Django 3.2.5 on 2021-07-24 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.AddField(
            model_name='cart',
            name='session_id',
            field=models.CharField(max_length=255, null=True),
        ),
    ]