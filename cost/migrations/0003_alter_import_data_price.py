# Generated by Django 4.0 on 2021-12-24 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cost', '0002_alter_exeldocument_doc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='import_data',
            name='price',
            field=models.FloatField(),
        ),
    ]
