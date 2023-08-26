# Generated by Django 4.1.4 on 2023-08-26 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aayesapp', '0006_rename_field_of_intrest_application_community_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='password',
            field=models.CharField(default='admin', max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='id',
            field=models.CharField(editable=False, max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='application',
            name='role',
            field=models.CharField(choices=[('DC', 'District Coordinator'), ('ADC', 'Associate District Coordinator'), ('ZC', 'Zonal District Coordinator'), ('SC', 'State Coordinator'), ('MBR', 'Member')], max_length=50),
        ),
    ]