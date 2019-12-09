from django.contrib.auth.models import User
from django.conf import settings
from django.db import models


class Project(models.Model):
	name = models.CharField(max_length=100, default='default title')
	user = models.ForeignKey(User, models.CASCADE, blank=True, null=True)
	description = models.CharField(max_length=300, default='default description')
	reward = models.DecimalField(max_digits=6, decimal_places=2, default='50.00')
	deadline = models.DateField(auto_now=False, auto_now_add=False, default='2019-01-01')

	def __str__(self):
		return self.name

class Task(models.Model):
	name = models.CharField(max_length=100)
	project = models.ForeignKey(Project, models.CASCADE, blank=True, null=True)
	reward = models.DecimalField(max_digits=6, decimal_places=2, default='50.00')
	isCompleted = models.BooleanField(default=False)
	# activeContributor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	description = models.CharField(max_length=300, default='default description')
	# @TODO --> Upload Cover Photo

	def __str__(self):
		return self.name
