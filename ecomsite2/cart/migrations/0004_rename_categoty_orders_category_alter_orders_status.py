# Generated by Django 4.2.5 on 2024-01-08 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_orders'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='categoty',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('confirm', 'confirm'), ('deliverd', 'deliverd')], default='pending', max_length=10),
        ),
    ]
