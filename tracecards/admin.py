from django.contrib import admin
from tracecards.models import Tracecard, Task, Cooperator

class TracecardAdmin(admin.ModelAdmin):
	date_hierarchy = "deadline"
	list_display = ("token", "topic")
	list_filter = ("client", "creator")

class CooperatorAdmin(admin.ModelAdmin):
	list_display = ("name", "task")
	list_filter = ("name", "task")

class CooperatorInline(admin.TabularInline):
	model = Cooperator
	extra = 2
	
class TaskAdmin(admin.ModelAdmin):
	inlines = [
		CooperatorInline,
	]

admin.site.register(Tracecard, TracecardAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Cooperator, CooperatorAdmin)