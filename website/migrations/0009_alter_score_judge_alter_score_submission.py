# Generated by Django 4.1.3 on 2022-11-30 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_alter_score_judge_alter_score_submission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='judge',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.judge'),
        ),
        migrations.AlterField(
            model_name='score',
            name='submission',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.submission'),
        ),
    ]
