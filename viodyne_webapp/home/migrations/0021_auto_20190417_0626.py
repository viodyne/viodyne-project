# Generated by Django 2.2 on 2019-04-17 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20190306_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=120)),
                ('Email', models.EmailField(max_length=120)),
                ('Comment', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ('Name',),
            },
        ),
        migrations.CreateModel(
            name='HomeS1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=120)),
                ('Image', models.ImageField(upload_to='s1/')),
            ],
            options={
                'ordering': ('Name',),
            },
        ),
        migrations.CreateModel(
            name='HomeS2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=120)),
                ('Name2', models.CharField(max_length=120)),
                ('Text', models.CharField(max_length=300)),
                ('Image', models.ImageField(upload_to='s2/')),
            ],
        ),
        migrations.CreateModel(
            name='Homes3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=120)),
                ('Image', models.ImageField(upload_to='s3/')),
            ],
            options={
                'ordering': ('Name',),
            },
        ),
        migrations.AlterModelOptions(
            name='contactus',
            options={'ordering': ('NAME',)},
        ),
        migrations.AlterModelOptions(
            name='homeslide3',
            options={'ordering': ('Name',)},
        ),
        migrations.AlterModelOptions(
            name='homeslider',
            options={'ordering': ('Name',)},
        ),
        migrations.AlterModelOptions(
            name='joinus',
            options={'ordering': ('FIRST_NAME',)},
        ),
    ]
