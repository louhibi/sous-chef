# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-01-15 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0034_auto_20170816_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='billing_payment_type',
            field=models.CharField(blank=True, choices=[(' ', '----'), ('3rd', '3rd Party'), ('credit', 'Credit card'), ('eft', 'EFT'), ('cash', 'Cash'), ('etransfert', 'e-Transfer'), ('cheque', 'Cheque')], max_length=10, null=True, verbose_name='Payment Type'),
        ),
    ]