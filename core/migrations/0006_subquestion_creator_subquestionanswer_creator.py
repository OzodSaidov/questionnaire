# Generated by Django 4.0.1 on 2022-01-25 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_question_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='subquestion',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.interrogator'),
        ),
        migrations.AddField(
            model_name='subquestionanswer',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.interrogator'),
        ),
    ]
