# Generated by Django 3.2.13 on 2022-09-05 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_ledger_monthly'),
    ]

    operations = [
        migrations.AddField(
            model_name='ledger_vouchers',
            name='closingbalance',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ledger_vouchers',
            name='ledgervoucher_date',
            field=models.DateField(null=True),
        ),
    ]
