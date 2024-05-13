# Generated by Django 5.0.4 on 2024-05-05 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=20, null=True)),
                ('time_zone', models.CharField(max_length=50)),
                ('website', models.URLField(blank=True, null=True)),
                ('updated_at', models.DateTimeField()),
                ('updated_by', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=100)),
            ],
        ),
    ]
