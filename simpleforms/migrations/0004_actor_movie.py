# Generated by Django 3.2.5 on 2021-08-11 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleforms', '0003_alter_director_filial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('release_date', models.DateTimeField()),
                ('actors', models.ManyToManyField(to='simpleforms.Actor')),
            ],
        ),
    ]