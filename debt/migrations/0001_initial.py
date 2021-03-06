# Generated by Django 3.2 on 2021-10-18 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('warung', '0013_delete_debt'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('qty', models.IntegerField()),
                ('note', models.TextField(blank=True)),
                ('total_debt', models.IntegerField()),
                ('name_debt', models.ForeignKey(max_length=70, on_delete=django.db.models.deletion.CASCADE, to='warung.good')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
