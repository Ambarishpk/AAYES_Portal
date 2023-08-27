# Generated by Django 4.1.4 on 2023-08-27 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aayesapp', '0015_alter_application_additional_skills_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='additional_skills',
            field=models.CharField(default='NA', max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='affiliated_to_any_political_party',
            field=models.CharField(default='NA', max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='affiliated_with_any_ngo_or_trust',
            field=models.CharField(default='NA', max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='believe_in_god',
            field=models.CharField(default='NA', max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='believe_in_rituals',
            field=models.CharField(default='NA', max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='call_brahmins_for_rituals',
            field=models.CharField(default='NA', max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='cause_for_untouchability',
            field=models.CharField(default='NA', max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='do_you_agree_that_conversion_is_a_solution_for_untouchability',
            field=models.CharField(default='NA', max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='father_or_spouse_monthly_income',
            field=models.CharField(default='NA', max_length=15),
        ),
        migrations.AlterField(
            model_name='application',
            name='father_or_spouse_name',
            field=models.CharField(default='NA', max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='father_or_spouse_occupation',
            field=models.CharField(default='NA', max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='hobby',
            field=models.CharField(default='NA', max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='hours_can_dedicate',
            field=models.CharField(default='NA', max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='how_many_assistant_district_coordinators_you_can_gather',
            field=models.CharField(default='NA', max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='invoved_in_any_social_activities',
            field=models.CharField(default='NA', max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='is_untouchability_prevalent_nowadays',
            field=models.CharField(default='NA', max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='main_problem_of_dalits',
            field=models.CharField(default='NA', max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='marital_status',
            field=models.CharField(default='NA', max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='money_can_you_donate_per_month',
            field=models.CharField(default='NA', max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='monthly_income',
            field=models.CharField(default='NA', max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='number_of_children',
            field=models.CharField(default='NA', max_length=10),
        ),
        migrations.AlterField(
            model_name='application',
            name='own_vehicle',
            field=models.CharField(default='NA', max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='read_ambedkar_books',
            field=models.CharField(default='NA', max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='religion',
            field=models.CharField(default='NA', max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='social_media_account',
            field=models.CharField(default='NA', max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='solution_for_untouchability_your_pov',
            field=models.CharField(default='NA', max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='solution_given_by_dr_ambedkar_for_untouchability',
            field=models.CharField(default='NA', max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='untouchability_related_to_religion',
            field=models.CharField(default='NA', max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='willing_to_attend_residential_training_programs',
            field=models.CharField(default='NA', max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='willing_to_visit_adw_hostels',
            field=models.CharField(default='NA', max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='willing_to_volunteer_for_free',
            field=models.CharField(default='NA', max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='worship_of_heirlooms',
            field=models.CharField(default='NA', max_length=50),
        ),
    ]
