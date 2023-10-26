# Generated by Django 4.2.3 on 2023-10-22 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0004_alter_sector_lugar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_localidad', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Localidad',
                'verbose_name_plural': 'Localidades',
            },
        ),
        migrations.AlterField(
            model_name='lugar',
            name='nombre_lugar',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='sector',
            name='lugar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus.lugar'),
        ),
        migrations.AlterField(
            model_name='sector',
            name='nombre_sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus.localidad'),
        ),
    ]
