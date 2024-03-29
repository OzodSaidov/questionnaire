# Generated by Django 4.0.1 on 2022-01-26 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_question_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subquestion',
            name='creator',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.interrogator'),
        ),
        migrations.AlterField(
            model_name='subquestionanswer',
            name='creator',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.interrogator'),
        ),
    ]
