# Generated by Django 2.1.5 on 2019-03-06 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20190306_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='TELEPHONE',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='joinus',
            name='TELEPHONE',
            field=models.CharField(max_length=120),
        ),
    ]
