# Generated by Django 5.0.7 on 2024-10-25 16:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign_id', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('lead_generated', models.IntegerField()),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('revenue_generated', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('cost_per_lead', models.DecimalField(blank=True, decimal_places=3, max_digits=10)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead_id', models.CharField(max_length=300, unique=True)),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('source', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('assigned_to', models.CharField(blank=True, max_length=255)),
                ('priority', models.IntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')], default=1)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leads', to='metrics.campaign')),
            ],
        ),
    ]
