# Generated by Django 2.1.5 on 2019-03-06 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20190306_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joinus',
            name='TELEPHONE',
            field=models.CharField(max_length=120),
        ),
    ]
