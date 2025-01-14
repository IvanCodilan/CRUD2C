# Generated by Django 5.0.6 on 2024-07-07 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_remove_item_children_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='agency_employee_no',
            field=models.IntegerField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='gsis_id',
            field=models.IntegerField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='mobile_no',
            field=models.IntegerField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='item',
            name='pagibig_id',
            field=models.IntegerField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='philhealth_no',
            field=models.IntegerField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='res_zipcode',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='spouse_telephone_no',
            field=models.IntegerField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='sss_no',
            field=models.IntegerField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='telephone_no',
            field=models.IntegerField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='tin_no',
            field=models.IntegerField(max_length=50, null=True),
        ),
    ]
