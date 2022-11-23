from django.db import models

class session(models.Model):
    id = models.CharField(max_length=8, primary_key=True)