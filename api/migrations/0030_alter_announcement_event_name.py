# Generated by Django 3.2.5 on 2021-07-20 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_alter_register_event_event_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='event_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.event'),
        ),
    ]
