# Generated by Django 5.0.6 on 2024-06-08 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_alter_taskitem_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskitem',
            name='image',
        ),
    ]
