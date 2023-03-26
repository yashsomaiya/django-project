# Generated by Django 4.1.7 on 2023-03-25 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingApp', '0003_contactnumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weddingbooking',
            name='payment_status',
        ),
        migrations.AddField(
            model_name='weddingbooking',
            name='location',
            field=models.CharField(default='windsor', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weddingbooking',
            name='payment_currency',
            field=models.CharField(choices=[('CAD', 'CAD'), ('USD', 'USD'), ('INR', 'INR')], default='CAD', max_length=10),
        ),
    ]