# Generated by Django 2.1.2 on 2018-10-12 07:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('scdownload', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='history',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
