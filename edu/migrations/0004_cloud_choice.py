# Generated by Django 3.2.19 on 2023-06-09 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0003_surveyanswer_surveyquestion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cloud_Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cloud_choice_images')),
                ('content', models.TextField()),
                ('title', models.CharField(max_length=255)),
            ],
        ),
    ]