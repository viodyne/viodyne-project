# Generated by Django 2.1.5 on 2019-03-06 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20190306_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joinus',
            name='TELEPHONE',
            field=models.CharField(max_length=20),
        ),
    ]
