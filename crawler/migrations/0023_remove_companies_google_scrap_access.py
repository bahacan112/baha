# Generated by Django 4.1.4 on 2023-01-20 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0022_accountreport_owner_companies_google_scrap_access_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companies',
            name='google_scrap_access',
        ),
    ]