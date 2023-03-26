# Generated by Django 4.1.7 on 2023-03-25 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingApp', '0004_remove_weddingbooking_payment_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weddingbooking',
            name='customer',
        ),
        migrations.AddField(
            model_name='weddingbooking',
            name='email',
            field=models.EmailField(default='abc', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weddingbooking',
            name='name',
            field=models.CharField(default='abc', max_length=122),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weddingbooking',
            name='phone',
            field=models.CharField(default='abc', max_length=20),
            preserve_default=False,
        ),
    ]