from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
	creator = models.ForeignKey(User)
	name = models.CharField(max_length=255)
	client = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	
	class Meta:
		abstract=True

class MainProject(Project):
	def __unicode__(self):
		return self.name
	
class SubProject(Project):
	main_project = models.ForeignKey(MainProject)
	
	def __unicode__(self):
		return self.name

class IssueItem(models.Model):
	PRIORITY_CHOICES = (
		(1, "critical"),
		(2, "high"),
		(3, "medium"),
		(4, "low"),
		(5, "remind"),
	)
	APPROVAL_CHOICES = (
		(0, "not public"),
		(1, "intern"),
		(2, "extern"),
	)
	CONDITION_CHOICES = (
		(0, "deleted"),
		(1, "active"),
		(2, "postponed"),
		(3, "invalid"),
	)
	subproject = models.ForeignKey(SubProject)
	creator = models.ForeignKey(User)
	module = models.CharField(max_length=50)
	topic = models.CharField(max_length=50)
	predecessor = models.PositiveIntegerField(blank=True, null=True)
	successor = models.PositiveIntegerField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	due = models.DateField(blank=True, null=True)
	priority = models.PositiveIntegerField(default=5, choices=PRIORITY_CHOICES)
	description = models.TextField()
	responsible_staff_member = models.CharField(max_length=255, blank=True)
	responsible_project_member = models.CharField(max_length=255)
	assistance = models.CharField(max_length=255)
	troubleshooting = models.TextField(blank=True)
	comment = models.TextField(blank=True)
	approval = models.PositiveIntegerField(default=0, choices=APPROVAL_CHOICES)
	condition = models.PositiveIntegerField(default=1, choices=CONDITION_CHOICES)
	
	class Meta:
		abstract=True

class Milestone(IssueItem):
	status = models.PositiveIntegerField(default=0, blank=True)
	
	def __unicode__(self):
		return self.description
	
class OpenIssue(IssueItem):
	STATUS_CHOICES = (
		(0,   "0%"),
		(10,  "10%"),
		(25,  "25%"),
		(40,  "40%"),
		(50,  "50%"),
		(60,  "60%"),
		(75,  "75%"),
		(90,  "90%"),
		(100, "100%"),
	)
	milestone = models.ForeignKey(Milestone, blank=True, null=True)
	status = models.PositiveIntegerField(default=0, choices=STATUS_CHOICES)
	
	def __unicode__(self):
		return self.description
