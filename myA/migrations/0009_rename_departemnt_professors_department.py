# Generated by Django 5.0.2 on 2024-03-27 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myA', '0008_professors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='professors',
            old_name='departemnt',
            new_name='department',
        ),
    ]
