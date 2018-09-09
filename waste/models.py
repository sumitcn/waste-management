from django.db import models
from account.models import User

class complainform(models.Model):
	dustbin_choice = (
        ('Sadar', 'Sadar'),
        ('Russell', 'Russell'),
        ('Reliance', 'Reliance'),
        )
	dustbin = models.CharField(max_length = 255 , choices = dustbin_choice )
	subject = models.CharField(max_length = 255)
	date = models.DateTimeField(auto_now = True)
	complain = models.TextField()

