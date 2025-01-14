# Generated by Django 5.0.6 on 2024-07-05 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_item_email_item_mobile_no_item_permanent_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='permanent_address',
        ),
        migrations.RemoveField(
            model_name='item',
            name='residential_address',
        ),
        migrations.AddField(
            model_name='item',
            name='per_barangay',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='per_city',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='per_house_no',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='per_province',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='per_street',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='per_subdivision',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='per_zipcode',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='res_barangay',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='res_city',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='res_house_no',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='res_province',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='res_street',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='res_subdivision',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='res_zipcode',
            field=models.TextField(blank=True, null=True),
        ),
    ]
