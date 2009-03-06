from django.db import models
from django.contrib.auth.models import User	

class Tracecard(models.Model):
	creator = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	client = models.CharField(max_length=30)
	contact_name = models.CharField(max_length=100)
	contact_email = models.CharField(max_length=100)
	token = models.CharField(unique=True, max_length=30)
	topic = models.CharField(max_length=30)
	domain = models.CharField(max_length=30)
	offer = models.CharField(max_length=10, blank=True)
	order = models.CharField(max_length=10, blank=True)
	status = models.CharField(max_length=30, default="in_process")
	deadline = models.DateField() #datetime.now + 14?
	description = models.TextField()
	#signed_by boolean or string?
	
	def __unicode__(self):
		return self.token
		
	class Meta:
		ordering = ['deadline']
		
class Task(models.Model):
	OFFER_TYPE_CHOICES = (
		("after_expenses", "after expenses"),
		("fix", "fix"),
	)
	tracecard = models.ForeignKey(Tracecard)
	token = models.CharField(unique=True, max_length=30)
	offer_type = models.CharField(max_length=30, choices=OFFER_TYPE_CHOICES)
	summary = models.CharField(max_length=100)
	description = models.TextField()
	
	def __unicode__(self):
		return self.token
		
class Cooperator(models.Model):
	task = models.ForeignKey(Task)
	name = models.CharField(max_length=30)
	hours_to_schedule = models.DecimalField(max_digits=5, decimal_places=2)
	hours_to_invoice = models.DecimalField(max_digits=5, decimal_places=2)
	
	def __unicode__(self):
		return self.name
