# Generated by Django 4.1.4 on 2023-08-27 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aayesapp', '0011_alter_application_password_alter_member_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='do_you_think_untouchability_related_to_religion',
            new_name='hours_can_dedicate',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='hours_can_you_dedicate',
            new_name='solution_for_untouchability_your_pov',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='solution_for_untouchability_in_your_pov',
            new_name='untouchability_related_to_religion',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='do_you_think_untouchability_related_to_religion',
            new_name='solution_for_untouchability_your_pov',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='solution_for_untouchability_in_your_pov',
            new_name='untouchability_related_to_religion',
        ),
    ]