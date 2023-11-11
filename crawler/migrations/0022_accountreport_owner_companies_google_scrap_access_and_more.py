# Generated by Django 4.1.4 on 2023-01-20 10:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crawler', '0021_alter_accountreport_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountreport',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı'),
        ),
        migrations.AddField(
            model_name='companies',
            name='google_scrap_access',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='accountreport',
            name='number',
            field=models.IntegerField(verbose_name='sayı'),
        ),
        migrations.AlterField(
            model_name='accountreport',
            name='report_date',
            field=models.DateField(verbose_name='son yenileme tarihi'),
        ),
        migrations.AlterField(
            model_name='accountreport',
            name='user',
            field=models.CharField(max_length=250, verbose_name='hesab ismi'),
        ),
        migrations.AlterField(
            model_name='accountreport',
            name='user_type',
            field=models.CharField(max_length=25, verbose_name='hesab tipi'),
        ),
    ]
