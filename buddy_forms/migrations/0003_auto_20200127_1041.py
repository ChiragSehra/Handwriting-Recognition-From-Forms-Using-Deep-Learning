# Generated by Django 2.1.5 on 2020-01-27 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buddy_forms', '0002_auto_20200127_1039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rotationangles',
            old_name='error',
            new_name='errors',
        ),
        migrations.AddField(
            model_name='rotationangles',
            name='document_type',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
