# Generated by Django 2.1.5 on 2019-02-14 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_contactus_joinus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='TELEPHONE',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='joinus',
            name='TELEPHONE',
            field=models.IntegerField(),
        ),
    ]
