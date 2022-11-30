# Generated by Django 4.1.3 on 2022-11-30 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_alter_score_judge_alter_score_submission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='judge',
        ),
        migrations.RemoveField(
            model_name='score',
            name='submission',
        ),
        migrations.AddField(
            model_name='score',
            name='judge',
            field=models.ManyToManyField(to='website.judge'),
        ),
        migrations.AddField(
            model_name='score',
            name='submission',
            field=models.ManyToManyField(to='website.submission'),
        ),
    ]
