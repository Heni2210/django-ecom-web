# Generated by Django 3.1.6 on 2021-02-17 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField(max_length=200)),
                ('image', models.ImageField(max_length=200, upload_to='')),
                ('type', models.CharField(max_length=200)),
            ],
        ),
    ]
