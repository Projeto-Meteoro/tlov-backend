# Generated by Django 4.1.7 on 2023-03-26 12:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('power', models.DecimalField(blank=True, decimal_places=1, max_digits=3)),
                ('equipment', models.CharField(max_length=50)),
                ('status', models.BooleanField()),
            ],
            options={
                'ordering': ['data_created'],
            },
        ),
    ]
