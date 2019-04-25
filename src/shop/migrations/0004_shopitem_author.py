# Generated by Django 2.1.7 on 2019-04-25 17:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0003_shopitem_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopitem',
            name='author',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
