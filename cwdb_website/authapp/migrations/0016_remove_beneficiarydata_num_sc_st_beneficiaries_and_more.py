# Generated by Django 4.2.6 on 2023-12-23 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0015_beneficiarydata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beneficiarydata',
            name='num_sc_st_beneficiaries',
        ),
        migrations.AddField(
            model_name='beneficiarydata',
            name='num_bpl_beneficiaries',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='beneficiarydata',
            name='num_sc_beneficiaries',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='beneficiarydata',
            name='num_st_beneficiaries',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='beneficiarydata',
            name='num_beneficiaries',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='beneficiarydata',
            name='num_females',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='beneficiarydata',
            name='num_general_beneficiaries',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='beneficiarydata',
            name='num_males',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='beneficiarydata',
            name='num_obc_beneficiaries',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='beneficiarydata',
            name='num_other_gender',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='beneficiarydata',
            name='state_of_beneficiaries',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
