# Generated by Django 4.1.4 on 2023-08-26 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aayesapp', '0009_alter_application_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='password',
            field=models.CharField(default='admin', max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='approved_by_dc',
            field=models.BooleanField(default=True, editable=False),
        ),
        migrations.AlterField(
            model_name='member',
            name='approved_by_sc',
            field=models.BooleanField(default=True, editable=False),
        ),
        migrations.AlterField(
            model_name='member',
            name='approved_by_zc',
            field=models.BooleanField(default=True, editable=False),
        ),
        migrations.AlterField(
            model_name='member',
            name='id',
            field=models.CharField(editable=False, max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='member',
            name='role',
            field=models.CharField(choices=[('DC', 'District Coordinator'), ('ADC', 'Associate District Coordinator'), ('ZC', 'Zonal District Coordinator'), ('SC', 'State Coordinator'), ('MBR', 'Member')], max_length=50),
        ),
    ]
