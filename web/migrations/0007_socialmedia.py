# Generated by Django 4.0.4 on 2023-02-07 07:21

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_portfolio_delete_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='Banner/', verbose_name='Image')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Social Media',
            },
        ),
    ]
