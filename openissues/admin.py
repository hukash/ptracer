from django.contrib import admin
from openissues.models import MainProject, SubProject, OpenIssue

admin.site.register(MainProject)
admin.site.register(SubProject)
admin.site.register(OpenIssue)
	