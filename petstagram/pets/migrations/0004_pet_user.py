# Generated by Django 3.2.3 on 2021-09-03 20:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pets', '0003_auto_20210711_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='accounts.petstagramuser'),
            preserve_default=False,
        ),
    ]
