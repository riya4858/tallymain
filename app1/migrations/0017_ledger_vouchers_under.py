# Generated by Django 3.2.13 on 2022-09-05 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_remove_ledger_vouchers_ledgervoucher_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='ledger_vouchers',
            name='under',
            field=models.CharField(max_length=225, null=True),
        ),
    ]
