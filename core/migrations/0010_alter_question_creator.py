# Generated by Django 4.0.1 on 2022-01-26 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_subquestion_creator_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.interrogator'),
        ),
    ]