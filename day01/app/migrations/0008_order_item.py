# Generated by Django 5.0.7 on 2024-07-13 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='item',
            field=models.ManyToManyField(to='app.item'),
        ),
    ]
