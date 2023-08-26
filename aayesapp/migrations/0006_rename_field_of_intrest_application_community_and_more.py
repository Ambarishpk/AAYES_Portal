# Generated by Django 4.1.4 on 2023-08-26 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aayesapp', '0005_rename_members_member'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='field_of_intrest',
            new_name='community',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='hours_can_you_dedicate_in_a_week',
            new_name='do_you_think_untouchability_related_to_religion',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='member_of',
            new_name='hobby',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='how_much_money_can_donate_per_month',
            new_name='hours_can_you_dedicate',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='previous_experience',
            new_name='module_of_interest',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='solution_for_untouchability_your_pov',
            new_name='money_can_you_donate_per_month',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='untouchability_related_to_religion',
            new_name='solution_for_untouchability_in_your_pov',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='field_of_intrest',
            new_name='community',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='hours_can_you_dedicate_in_a_week',
            new_name='do_you_think_untouchability_related_to_religion',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='member_of',
            new_name='hobby',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='how_much_money_can_donate_per_month',
            new_name='hours_can_you_dedicate',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='previous_experience',
            new_name='module_of_interest',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='solution_for_untouchability_your_pov',
            new_name='money_can_you_donate_per_month',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='untouchability_related_to_religion',
            new_name='solution_for_untouchability_in_your_pov',
        ),
        migrations.RemoveField(
            model_name='application',
            name='willing_to_attend_workshop',
        ),
        migrations.RemoveField(
            model_name='application',
            name='willing_to_pay_workshop_registration_fee',
        ),
        migrations.RemoveField(
            model_name='member',
            name='willing_to_attend_workshop',
        ),
        migrations.RemoveField(
            model_name='member',
            name='willing_to_pay_workshop_registration_fee',
        ),
        migrations.AlterField(
            model_name='application',
            name='father_or_spouse_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='father_or_spouse_occupation',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='invoved_in_any_social_activities',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='languages_spoken',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='main_problem_of_dalits',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='marital_status',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='monthly_income',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='number_of_children',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='member',
            name='father_or_spouse_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='father_or_spouse_occupation',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='invoved_in_any_social_activities',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='languages_spoken',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='main_problem_of_dalits',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='marital_status',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='monthly_income',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='number_of_children',
            field=models.CharField(max_length=10),
        ),
    ]