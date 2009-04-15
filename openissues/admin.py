from django.contrib import admin
from openissues.models import MainProject, SubProject, Milestone, OpenIssue

admin.site.register(MainProject)
admin.site.register(SubProject)
admin.site.register(Milestone)
admin.site.register(OpenIssue)
	