# Generated by Django 3.1.4 on 2021-01-02 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_matricula_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matricula',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.grupo'),
        ),
    ]
