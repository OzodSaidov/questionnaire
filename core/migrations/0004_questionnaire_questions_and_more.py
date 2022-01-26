# Generated by Django 4.0.1 on 2022-01-25 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_questionnaire_questions_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='questions',
            field=models.ManyToManyField(to='core.Question'),
        ),
        migrations.AlterField(
            model_name='resultquestionnaire',
            name='question_answer',
            field=models.CharField(max_length=3),
        ),
    ]
