from django.db import models
from django.contrib.auth.models import User

class MainProject(models.Model):
    creator = models.ForeignKey(User)
    name = models.Charfield(max_length=255)
    client = models.Charfield(max_length=100)

	def __unicode__(self):
	    return self.label	

class SubProject(models.Model):
    main_project = models.ForeignKey(MainProject)
	creator = models.ForeignKey(User)
	label = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	client = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.label
	
class OpenIssue(models.Model):
	STATUS_CHOICES = (
		(0,    "0%"),
		(10,  "10%"),
		(25,  "25%"),
		(40,  "40%"),
		(50,  "50%"),
		(60,  "60%"),
		(75,  "75%"),
		(90,  "90%"),
		(100,"100%"),
	)
    PRIORITY_CHOICES = (
        (1, "critical"),
        (2, "high"),
        (3, "medium"),
        (4, "low"),
        (5, "remind"),
    )
	APPROVAL_CHOICES = (
		(0, "secret"),
		(1, "intern"),
		(2, "extern"),
	)
	subproject = models.ForeignKey(SubProject)
	creator = models.ForeignKey(User)
	module = models.CharField(max_length=50)
	topic = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	scheduled_for = models.DateField(blank=True)
	priority = models.PositiveIntegerField(default=5, choices=PRIORITY_CHOICES)
    description = models.TextField()
	responsible_staff_member = models.CharField(max_length=255, blank=True)
	responsible_project_member = models.CharField(max_length=255)
	assistance = models.CharField(max_length=255)
	status = models.PositiveIntegerField(default=0, choices=STATUS_CHOICES)
	troubleshooting = models.TextField(blank=True)
	comment = models.TextField(blank=True)
	approval = models.PositiveIntegerField(default=0, choices=APPROVAL_CHOICES)
	
	def __unicode__(self):
		return self.description
