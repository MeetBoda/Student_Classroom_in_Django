# Generated by Django 4.1.5 on 2023-03-10 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='material_title',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
