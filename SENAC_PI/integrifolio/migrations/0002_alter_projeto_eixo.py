# Generated by Django 4.1.4 on 2022-12-28 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('integrifolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='eixo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eixos', to='integrifolio.eixo'),
        ),
    ]