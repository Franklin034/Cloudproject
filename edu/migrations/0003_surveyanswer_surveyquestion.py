# Generated by Django 3.2.19 on 2023-06-08 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0002_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SurveyAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(choices=[('Agreed', 'Agreed'), ('Maybe', 'Maybe'), ('Disagreed', 'Disagreed')], max_length=200)),
                ('recommendation', models.TextField(blank=True)),
                ('grade', models.IntegerField(choices=[(2, 'Agreed'), (1, 'Maybe'), (0, 'Disagreed')])),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edu.surveyquestion')),
            ],
        ),
    ]
