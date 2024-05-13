# Generated by Django 5.0.4 on 2024-05-11 04:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Service Name')),
                ('description', models.TextField(verbose_name='Service Description')),
                ('service_letter', models.CharField(help_text='Initial letter for service identification', max_length=1, verbose_name='Service Letter')),
                ('is_active', models.BooleanField(default=True, verbose_name='Service Status')),
                ('desks', models.IntegerField(default=1, verbose_name='Number of Desks')),
                ('waiting_time_sla', models.IntegerField(default=0, help_text='Service Level Agreement for waiting time in minutes', verbose_name='Waiting Time SLA (min)')),
                ('serving_time_sla', models.IntegerField(default=0, help_text='Service Level Agreement for serving time in minutes', verbose_name='Serving Time SLA (min)')),
                ('duration', models.IntegerField(default=0, help_text='Estimated duration of the service in minutes', verbose_name='Service Duration (min)')),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='agent_count',
            field=models.IntegerField(default=0, verbose_name='Number of Agents'),
        ),
        migrations.AddField(
            model_name='branch',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email Address'),
        ),
        migrations.AddField(
            model_name='branch',
            name='mobile',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Mobile Number'),
        ),
        migrations.AddField(
            model_name='branch',
            name='telephone',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Telephone Number'),
        ),
        migrations.AddField(
            model_name='branch',
            name='service_areas',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='company.servicearea', verbose_name='Service Areas'),
            preserve_default=False,
        ),
    ]
