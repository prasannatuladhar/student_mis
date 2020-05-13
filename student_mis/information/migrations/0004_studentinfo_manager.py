# Generated by Django 2.2 on 2020-05-13 04:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('information', '0003_auto_20200513_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='manager',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
