# Generated by Django 4.0.4 on 2023-02-07 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_update'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
                ('answer', models.CharField(max_length=500)),
            ],
        ),
    ]