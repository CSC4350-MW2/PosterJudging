from django.db import models


class judge(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    panther_id = models.CharField(max_length=9, primary_key=True, unique=True)
    subject_choices = [
        ('CSC', 'Computer Science'),
        ('PHY', 'Physics'),
        ('BIO', 'Biology'),
        ('CHEM', 'Chemistry'),
    ]
    subject = models.CharField(max_length=4, choices=subject_choices)
    level_choices = [
        ('Grad', 'Graduate Student'),
        ('Prof', 'Professor'),
    ]
    level = models.CharField(max_length=4, choices=level_choices)


class submission(models.Model):
    subject_choices = [
        ('CSC', 'Computer Science'),
        ('PHY', 'Physics'),
        ('BIO', 'Biology'),
        ('CHEM', 'Chemistry'),
    ]
    subject = models.CharField(max_length=4, choices=subject_choices)
    level_choices = [
        ('Undr', 'Undergraduate Student'),
        ('Grad', 'Graduate Student'),
    ]
    level = models.CharField(max_length=4, choices=level_choices)

class session(models.Model):
    id = models.CharField(max_length=8, primary_key=True)
    judges = models.ManyToManyField(judge)
    submissions = models.ManyToManyField(submission)