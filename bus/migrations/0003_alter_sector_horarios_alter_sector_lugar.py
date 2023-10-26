# Generated by Django 4.2.3 on 2023-10-19 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0002_alter_sector_horarios_alter_sector_lugar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sector',
            name='horarios',
            field=models.ManyToManyField(to='bus.horario'),
        ),
        migrations.AlterField(
            model_name='sector',
            name='lugar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus.lugar'),
        ),
    ]
