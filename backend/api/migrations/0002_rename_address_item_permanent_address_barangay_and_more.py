# Generated by Django 5.0.6 on 2024-07-05 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='address',
            new_name='permanent_address_barangay',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='last_name',
            new_name='surname',
        ),
        migrations.RemoveField(
            model_name='item',
            name='phone',
        ),
        migrations.AddField(
            model_name='item',
            name='agency_employee_no',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='blood_type',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='civil_status',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='gsis_id',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='height',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='mobile_no',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='pagibig_id',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='permanent_address_city',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='permanent_address_house_no',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='permanent_address_province',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='permanent_address_street',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='permanent_address_subdivision',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='permanent_address_zip_code',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='philhealth_no',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='place_of_birth',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='residential_address_barangay',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='residential_address_city',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='residential_address_house_no',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='residential_address_province',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='residential_address_street',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='residential_address_subdivision',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='residential_address_zip_code',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='sex',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='sss_no',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='telephone_no',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='tin_no',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]