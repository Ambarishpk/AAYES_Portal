# Generated by Django 4.1.4 on 2023-08-26 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aayesapp', '0002_rename_do_you_agree_that_converion_is_a_solution_for_untouchability_application_do_you_agree_that_co'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='approved_by_dc',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='application',
            name='approved_by_sc',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='application',
            name='approved_by_zc',
            field=models.BooleanField(default=False),
        ),
    ]