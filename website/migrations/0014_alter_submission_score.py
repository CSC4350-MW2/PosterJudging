# Generated by Django 4.1.3 on 2022-11-30 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_alter_submission_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='score',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]